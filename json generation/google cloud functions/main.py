import functions_framework
import codecs
import random
from datetime import datetime
import xml.etree.ElementTree as ET
import os
import json
import csv
import pygsheets
import unicodedata



## google drive folder / team drive IDs
# folder where level-by-level levelgens are
drivefolder = "18SRLdZK-n2QismpXY1Cn-FFqrJutIU8I"
# folder where json files are
jsonfolder = "1XwKKuBPLbHl93ba95XjEDzdqq8RgntYj"
teamid = "0AArPHFZAiZRmUk9PVA"


## client secrets location
secfile = './client_secret.json'



@functions_framework.http
def hello_http(request):
	"""HTTP Cloud Function.
	Args:
	    request (flask.Request): The request object.
	    <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
	Returns:
	    The response text, or any set of values that can be turned into a
	    Response object using `make_response`
	    <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
	"""
	## main code
	# connect to google sheets api
	gc = pygsheets.authorize(service_file=secfile)
	gc.drive.enable_team_drive(teamid);

	#get arguments from the url
	request_json = request.get_json(silent=True)
	request_args = request.args

	#check for action in arguments, default to list
	if request_json and 'act' in request_json:
		command = request_json['act']
	elif request_args and 'act' in request_args:
		command = request_args['act']
	else:
		command = 'list'

	#fetch sheet id, default to None
	if request_json and 'sheet' in request_json:
		sheetid = request_json['sheet']
	elif request_args and 'act' in request_args:
		sheetid = request_args['sheet']
	else:
		sheetid = None

	#handle each command
	if (command == "list"):
		return slist(gc);
	elif (command == "fetch"):
		return fetch(gc,sheetid);
	elif (command == "generate"):
		return generate(gc,sheetid);
	else:
		return "unknown command";

# lists the spreadsheet titles currently accessible
def slist(gc):
	resstr = gc.spreadsheet_titles()
	return resstr;

# return the values from a spreadsheet
def fetch(gc,sheetid):
	fetchedsheet = gc.open_by_key(sheetid);
	fetchedvalue = fetchedsheet[0].get_values("A1","B150")
	return fetchedvalue;

# utility function to remove spaces and turn things lowercase
def removeSpaces (lst):
	lst = [x.lstrip()for x in lst if x != ' ']
	lst = [x.strip() for x in lst if x != ' ']
	lst = [x.lower() for x in lst if x != ' ']
	return lst
# utility function to wrap each letter object as a StoneText
def cleanletter(lobj):
	# deal with alternate formats if coming from xml
	if (isinstance(lobj,str)):
		return {"StoneText": lobj}
	else:
		return {"StoneText": lobj['#text']}

# generate a foil stone based on the letters taught so far
def makeFoil (foilstones, levelletters, targetletter):
	foils = foilstones + levelletters + levelletters
	nf = targetletter
	# ideally return a foil stone that is Not the target letter
	while (nf == targetletter):
		nf = foils[random.randrange(len(foils))]
	return nf

def generate(gc, sheetid):
	res = [];
	# connect to the spreadsheet
	fetchedsheet = gc.open_by_key(sheetid);
	# fetch the level content cells
	fetchedvalue = fetchedsheet[0].get_values("A1","B150")
	# fetch the metadata cells
	fetchedmeta = fetchedsheet[1].get_values("A1","B20")
	# pull name and version information
	langname = fetchedmeta[0][1]
	majversion = int(fetchedmeta[1][1])
	minversion = int(fetchedmeta[2][1])
	# increment minor version
	minversion += 1
	variant = fetchedmeta[3][1]
	apptitle = fetchedmeta[4][1]
	# split feedback audios and texts into an array
	fbtext = fetchedmeta[5][1].split(",")
	fbaudio = fetchedmeta[6][1].split(",")
	rownum = 0;
	foilstones = [];
	# set location of existing level templates
	indir = './input_154/'
	cleanlangname = langname.lower()
	assetbase = "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/"

	# create the javascript object that will be converted to the json file
	bigobj = {"title": apptitle,"RightToLeft":False,"FeedbackTexts":fbtext,
	"majversion":majversion,"minversion":minversion,"langname":langname,"FeedbackAudios":fbaudio,
	"OtherAudios":{
		"Select your player": "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/Select-your-player.mp3",
		"Watch me grow": "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/watch-me-grow.mp3",
		"Are you sure": "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/are-you-sure.mp3"
	}}
	bigobj["Levels"] = [];
	# go through each row
	for row in fetchedvalue:
		levelbase = {};
		f = "level" + str(rownum) + ".xml"
		# parse the xml template for that level
		tree = ET.parse (os.path.join(indir,f))
		treeRoot = tree.getroot()
		group = int(treeRoot.get('LettersGroup'))
		leveltype = row[1]
		# copy over level type information
		fadeout = treeRoot.get('HideCallout')
		if (fadeout == "-1"):
			fadeout = 0;
		ptype = "Visible";
		ltype = "";
		if (leveltype == "match" or leveltype == "matchSound"):
			treeRoot.set('monsterInputType', "Letter")
			ltype = "LetterOnly"
		if (leveltype == "matchfirst"):
			treeRoot.set('monsterInputType', "LetterInWord")
			ltype = "LetterInWord"
		if (leveltype == "spell" or leveltype == "spellSound"):
			treeRoot.set('monsterInputType', "Word")
			ltype = "Word"
		if (leveltype == "matchSound" or leveltype == "spellSound"):
			ptype = "Hidden"
			fadeout = 0;
		#create javascript object for the level
		levelbase["LevelMeta"] = {
		"LevelNumber":rownum, "PromptType":ptype,
		"LevelType":ltype, "csvType":leveltype,
		"PromptFadeout": fadeout, "LetterGroup": group}
		messylettersinlevel = row[0].split(",")
		lettersinlevel = [x for x in messylettersinlevel if x !=' ']
		lettersinlevel = removeSpaces(lettersinlevel)
		# initialize empty arrays
		targets = []
		audionames = []
		foiltargets = []
		prompttexts = []
		# handle letter matching levels
		if (leveltype == "match" or leveltype == "matchSound"):
			for nl in lettersinlevel:
				# everything is just the target letter
				nl = nl.strip('[]').lower()
				if (nl not in foilstones):
					foilstones.append(nl)
				targets.append(cleanletter(nl))
				foiltargets.append(nl)
				audionames.append(nl)
				prompttexts.append(nl)
		# handle matchfirst levels
		if (leveltype == "matchfirst"):
			for nl in lettersinlevel:
				#seperate target from the rest of the word
				therest = []
				targ = nl[nl.find('(') + 1 : nl.find(')')]
				rl = nl[nl.find(')')+1:]
				therest.append(rl)
				targ = targ.strip('[]').lower()
				if (targ not in foilstones):
					foilstones.append(targ)
				targets.append(cleanletter(targ))
				audionames.append(targ)
				# print full word as prompt text
				prompttexts.append(targ + ''.join(therest))
				foiltargets.append(targ)

		# handle spell levels
		if (leveltype == "spell" or leveltype == "spellSound"):
			for nw in lettersinlevel:
				targ = []
				hw = ""
				lp = 0
				targo = []
				while (lp < len(nw) ):
					testlet = nw[lp]
					if (testlet == '['):
						lp+=1
						testlet = nw[lp]
						while (testlet != ']' and lp < len(nw)):
							hw += nw[lp]
							lp+=1
							testlet = nw[lp]
						targ.append(cleanletter(hw))
						targo.append(hw)
						foiltargets.append(hw)
						hw = ""
					else:
						targ.append(cleanletter(testlet))
						targo.append(testlet)
						foiltargets.append(testlet)
					lp += 1
				targets.append(targ)
				prompttexts.append(''.join(targo))
				audionames.append(''.join(targo))
		rownum += 1
		levelbase["Puzzles"] = [];
		xmpuz = treeRoot[0]
		sn = 0;
		# create each segment object
		for pt in targets:
			# make sure target is returned as an array
			if hasattr(pt, "__len__") and len(pt) > 1:
				npt = pt
			else:
				npt = [pt,]
			# build audio file url
			apth = assetbase + audionames[sn] + ".mp3"
			nseg = {"SegmentNumber": sn, "targetstones": npt,
			"prompt":{
			"PromptText":prompttexts[sn],
			"PromptAudio":apth
			}
			};
			fstones = [];
			# how many foil stones to generate?
			numfoil= len(xmpuz[sn].find("Stones"))
			for i in range(numfoil):
				nfoil = makeFoil(foilstones,foiltargets,pt)
				fstones.append(cleanletter(nfoil))
			sn = sn + 1
			nseg["foilstones"] = fstones
			levelbase["Puzzles"].append(nseg)
		bigobj["Levels"].append(levelbase)

	#post-generation!!

	# update min version number
	fetchedsheet[1].update_value("B3",minversion)
	now = datetime.now()
	# updated update time
	fetchedsheet[1].update_value("B8",now.strftime("%m/%d/%Y, %H:%M:%S"))

	#experimental - save a copy of this json file as a log
	with open("./logs/" + cleanlangname + "-" + str(majversion) + "-" + str(minversion) + ".json", "w") as json_file:

		json_file.write(json.dumps(bigobj))
		json_file.close()

	# output json object contents
	return json.dumps(bigobj);
