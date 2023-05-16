import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

class ContentDeliveryAgent:

    def __init__(self, course_content_id_list, delivery_interval):
        self.course_content_id_list = course_content_id_list
        self.delivery_interval = delivery_interval
        self.creds = None
        self.service = None

    def authenticate(self):
        # TODO: add your authentication code here
        pass

    def get_course_content(self, document_id):
        # TODO: Use Google Docs API to fetch the course content by document_id
        pass

    def deliver_content(self):
        self.authenticate()
        for document_id in self.course_content_id_list:
            content = self.get_course_content(document_id)
            # TODO: Deliver this content to the student via Discord bot
            time.sleep(self.delivery_interval * 60)  # Sleep for delivery_interval minutes
