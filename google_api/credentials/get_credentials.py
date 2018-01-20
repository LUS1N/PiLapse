import os
from oauth2client.file import Storage

def get_credentials(app_name):
    """Gets valid user credentials from storage.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   app_name + '-google-credentials.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials:
        raise ValueError('Credentials for %s are not set up, run create_credentials first.' % app_name) 

    return credentials
