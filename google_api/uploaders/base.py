from apiclient import discovery
import httplib2
from google_api.credentials import get_credentials as creds

class BaseUploader:

    def __init__(self, appName, apiName):
        self.credentials = creds.get_credentials(appName)
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build(apiName, 'v3', http=self.http)
