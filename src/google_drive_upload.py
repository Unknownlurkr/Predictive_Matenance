from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Set up the Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'credentials.json'

def upload_to_drive(file_path, mime_type='application/octet-stream'):
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': os.path.basename(file_path)}
    media = MediaFileUpload(file_path, mimetype=mime_type)
    
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    print(f'File ID: {file.get("id")}')

if __name__ == "__main__":
    file_path = 'data/sensor_data.csv'  # Update with your file path
    upload_to_drive(file_path)