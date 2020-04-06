from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GoogleAPI:
    def __init__(self, google_service = 'drive'):
        if google_service == 'sheets':
            SCOPES = 'https://www.googleapis.com/auth/spread{}'.format(google_service.lower())
        else:
            SCOPES = 'https://www.googleapis.com/auth/{}'.format(google_service.lower())
        self.SCOPES = [SCOPES]
        self.google_service = google_service.lower()
        self.credentials = self.getCredentials()
        self.service = self.build()
    def getCredentials(self):
        creds = None
        TOKEN = 'token{}.pickle'.format(self.google_service)
        CREDENTIALS = 'credentials{}.json'.format(self.google_service)
        if os.path.exists(TOKEN):
            with open(TOKEN, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, self.SCOPES)
                creds = flow.run_local_server(port=0)
            	# Save the credentials for the next run
            with open(TOKEN, 'wb') as token:
                pickle.dump(creds, token)
            return creds
    def build(self):
        try:
            if self.google_service == 'drive':
                return build(self.google_service, 'v3', credentials = self.credentials)
            elif self.google_service == 'sheets':
                return build(self.google_service, 'v4', credentials = self.credentials)
            else:
                return None
        except Exception as e:
            print(e)
            print('{} is invalid google service'.format(self.google_service))
            return None
