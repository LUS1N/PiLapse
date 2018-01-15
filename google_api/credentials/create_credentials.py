
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import argparse
parser = argparse.ArgumentParser(parents=[tools.argparser])
parser.add_argument( 'client_secret', help='Directory of the client_secret.json file.')
parser.add_argument('app_name', help='Name of the application.')
flags = parser.parse_args()

# If modifying these scopes, delete your previously saved credentials
SCOPES = 'https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/youtube.upload'
CLIENT_SECRET_FILE = flags.client_secret
APPLICATION_NAME = flags.app_name


def create_credentials():
    """Creates valid user credentials in storage.

    OAuth2 flow is completed to obtain the new credentials.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   APPLICATION_NAME +'-google-credentials.json')

    store = Storage(credential_path)
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    credentials = tools.run_flow(flow, store, flags)
    print('Storing credentials to ' + credential_path)

def main():
    """Creates and stores credentials file from client_secret.json file for the application.

    Credentials are stored at ~/.credentials/APP_NAME-google-credentials.json
    """
    create_credentials()

if __name__ == '__main__':
    main()