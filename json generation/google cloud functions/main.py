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

	gc = pygsheets.authorize(service_file=secfile)
	gc.drive.enable_team_drive(teamid);


	request_json = request.get_json(silent=True)
	request_args = request.args

	if request_json and 'act' in request_json:
		command = request_json['act']
	elif request_args and 'act' in request_args:
		command = request_args['act']
	else:
		command = 'list'

	if request_json and 'sheet' in request_json:
		sheetid = request_json['sheet']
	elif request_args and 'act' in request_args:
		sheetid = request_args['sheet']
	else:
		sheetid = None

	if (command == "list"):
		return slist(gc);
	elif (command == "fetch"):
		return fetch(gc,sheetid);
	elif (command == "generate"):
		return generate(gc,sheetid);
	else:
		return "unknown command";

def slist(gc):

	resstr = gc.spreadsheet_titles()
	return resstr;

def fetch(gc,sheetid):
	fetchedsheet = gc.open_by_key(sheetid);
	fetchedvalue = fetchedsheet[0].get_values("A1","B150")
	return fetchedvalue;


def removeSpaces (lst):
	lst = [x.lstrip()for x in lst if x != ' ']
	lst = [x.strip() for x in lst if x != ' ']
	lst = [x.lower() for x in lst if x != ' ']
	return lst
def cleanletter(lobj):
	if (isinstance(lobj,str)):
		return {"StoneText": lobj}
	else:
		return {"StoneText": lobj['#text']}
def makeFoil (foilstones, levelletters, targetletter):
	foils = foilstones + levelletters + levelletters
	nf = targetletter
	while (nf == targetletter):
		nf = foils[random.randrange(len(foils))]

	return nf

def generate(gc, sheetid):
	res = [];
	fetchedsheet = gc.open_by_key(sheetid);
	fetchedvalue = fetchedsheet[0].get_values("A1","B150")
	fetchedmeta = fetchedsheet[1].get_values("A1","B20")
	langname = fetchedmeta[0][1]
	majversion = int(fetchedmeta[1][1])
	minversion = int(fetchedmeta[2][1])
	minversion += 1
	variant = fetchedmeta[3][1]
	apptitle = fetchedmeta[4][1]
	fbtext = fetchedmeta[5][1].split(",")
	fbaudio = fetchedmeta[6][1].split(",")
	rownum = 0;
	foilstones = [];
	indir = './input_154/'
	cleanlangname = langname.lower()
	assetbase = "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/"
	bigobj = {"title": apptitle,"RightToLeft":False,"FeedbackTexts":fbtext,
	"majversion":majversion,"minversion":minversion,"langname":langname,"FeedbackAudios":fbaudio,
	"OtherAudios":{
		"Select your player": "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/Select-your-player.mp3",
		"Watch me grow": "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/watch-me-grow.mp3",
		"Are you sure": "https://feedthemonster.curiouscontent.org/lang/" + cleanlangname + "/audios/are-you-sure.mp3"
	}}
	bigobj["Levels"] = [];
	for row in fetchedvalue:
		levelbase = {};
		f = "level" + str(rownum) + ".xml"

		tree = ET.parse (os.path.join(indir,f))
		treeRoot = tree.getroot()
		group = int(treeRoot.get('LettersGroup'))
		leveltype = row[1]
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

		levelbase["LevelMeta"] = {
		"LevelNumber":rownum, "PromptType":ptype,
		"LevelType":ltype, "csvType":leveltype,
		"PromptFadeout": fadeout, "LetterGroup": group}
		messylettersinlevel = row[0].split(",")
		lettersinlevel = [x for x in messylettersinlevel if x !=' ']
		lettersinlevel = removeSpaces(lettersinlevel)
		targets = []
		audionames = []
		foiltargets = []
		prompttexts = []
		if (leveltype == "match" or leveltype == "matchSound"):
			for nl in lettersinlevel:
				nl = nl.strip('[]').lower()
				if (nl not in foilstones):
					foilstones.append(nl)
				targets.append(cleanletter(nl))
				foiltargets.append(nl)
				audionames.append(nl)
				prompttexts.append(nl)
		if (leveltype == "matchfirst"):

			for nl in lettersinlevel:
				therest = []
				targ = nl[nl.find('(') + 1 : nl.find(')')]
				#print(targ)
				rl = nl[nl.find(')')+1:]
				therest.append(rl)
				targ = targ.strip('[]').lower()
				if (targ not in foilstones):
					foilstones.append(targ)
				targets.append(cleanletter(targ))
				audionames.append(targ)
				prompttexts.append(targ + ''.join(therest))
				foiltargets.append(targ)
			#print (therest)

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
		for pt in targets:
			if hasattr(pt, "__len__") and len(pt) > 1:
				npt = pt
			else:
				npt = [pt,]
			apth = assetbase + audionames[sn] + ".mp3"
			nseg = {"SegmentNumber": sn, "targetstones": npt,
			"prompt":{
			"PromptText":prompttexts[sn],
			"PromptAudio":apth
			}
			};
			fstones = [];
			numfoil= len(xmpuz[sn].find("Stones"))
			for i in range(numfoil):
				nfoil = makeFoil(foilstones,foiltargets,pt)
				fstones.append(cleanletter(nfoil))
			sn = sn + 1
			nseg["foilstones"] = fstones
			levelbase["Puzzles"].append(nseg)
		bigobj["Levels"].append(levelbase)

	#post-generation
	fetchedsheet[1].update_value("B3",minversion)
	now = datetime.now()
	fetchedsheet[1].update_value("B8",now.strftime("%m/%d/%Y, %H:%M:%S"))
	with open("./logs/" + cleanlangname + "-" + str(majversion) + "-" + str(minversion) + ".json", "w") as json_file:

		json_file.write(json.dumps(bigobj))
		json_file.close()

	return json.dumps(bigobj);
