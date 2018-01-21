from apiclient import discovery
import httplib2
from google_api.credentials import get_credentials as creds

class BaseUploader:

    def __init__(self, appName, apiName):
        print('Getting credentials for %s' % appName)
        self.credentials = creds.get_credentials(appName)

        print('Authorizing...')
        self.http = self.credentials.authorize(httplib2.Http())

        print('Building %s service' % apiName)
        self.service = discovery.build(apiName, 'v3', http=self.http)
