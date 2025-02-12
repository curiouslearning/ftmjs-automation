## Google Apps Script

### Overview
This section describes the Google Apps Script associated with Google Sheets/Docs/Drive. These script is used to automate the levelgen sheet syntax checking processes in the Google sheets.

### Setup & Deployment

1. **Clone the repository**:
   Clone this repository to your local machine if you haven't already.

2. **Copy the App Script**:
   Open the .gs files from the repository.
   Copy the entire code of the .gs file that you want to deploy.

3. **Deploy to Google Sheets**:
   Open the Google Sheet where you want to deploy the script.
   In the Google Sheet, go to the Extensions menu → Apps Script.
   This will open the Google Apps Script editor. In the editor, paste the copied script code into the editor window.

4. **Save the Script**:
   After pasting the script code, click on the Save icon or press Ctrl + S to save the script.

5. **Deploy as Web App**:
   To deploy the script as a Web App, go to the Deploy button in the upper right corner of the Apps Script editor.
   Select Deploy as web app.
   In the deployment settings:
      Description: Provide a description for your web app.
      Execute as: Select Me (the owner).
      Who has access: Select Anyone or Anyone within your domain, depending on who you want to have access to the app.
   Click Deploy.
   You will be prompted to authorize the app. Click Review Permissions, select your Google account, and allow the necessary permissions.
   After successful deployment, you will receive a URL that is your Web App's URL.