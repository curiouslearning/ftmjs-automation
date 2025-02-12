## Content Checker

### Overview
The **Content Checker** script is designed to verify the presence of audio files referenced in a JSON file for a specific language. It compares the audio files listed in the JSON against the corresponding folder in **Google Drive**. The script ensures that all the required audio files are present in the Google Drive folder for that language, helping to avoid missing or incomplete content in the Levelgen system.

### How to Run Locally

To run the Content Checker script locally, follow these steps:

1. **Clone the Repository**

2. **Set Up the Environment**
    Ensure you have Python 3.x installed. Then, install the required dependencies by running:
    pip install -r requirements.txt

    **Or you can manually install the necessary libraries**:
    pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib requests smtplib

3. **Configure the Script**
    Place the credentials.json file you downloaded from your Google Cloud service account in the same directory as your script, or specify the path in the script:
    KEY_FILE = './credentials.json'

    **Update the Google Drive details and email credentials in the script**:
    shared_drive_id = 'your_shared_drive_id'
    root_folder_id = 'your_root_folder_id'
    desired_folder_id = 'your_desired_folder_id'
    gmail_user = 'your-email@example.com'
    gmail_app_password = 'your-app-password'

4. **Run the Script Locally**
    Now, you can run the script by executing the following command:
    python content_verification.py
5. **Verify Missing Audios**
The script will check the audio files in the specified Google Drive folder and compare them against the JSON data. If any files are missing, it will send an email to the specified recipients.