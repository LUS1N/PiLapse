from apiclient import discovery
from apiclient.http import MediaFileUpload

from google_api.uploaders.base import BaseUploader


class Drive(BaseUploader):

    def __init__(self, appName):
        BaseUploader.__init__(self, appName, "drive")

    def upload_file(self, root_id, file_name, file_path):
        file_metadata = {
            'name': file_name,
            'parents': [root_id]
        }

        file = self.service.files().create(body=file_metadata,
                                           media_body=file_path,
                                           fields='id, name').execute()
        return file

    def create_folder_in_root(self, folder_name):
        return self.create_folder('root', folder_name)

    def create_folder(self, root_id, folder_name):
        file_metadata = {
            'parents': [root_id],
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = self.service.files().create(
            body=file_metadata, fields='*').execute()
        return folder

    def get_all_files(self):
        results = self.service.files().list().execute()
        return results.get('files', [])

    def find_folders(self, name):
        q = "mimeType = 'application/vnd.google-apps.folder' and name = '%s' and trashed = false" % (
            name)
        response = self.service.files().list(
            q=q, fields='nextPageToken, files(id, name, trashed)').execute()

        return response.get('files', [])

    def find_folder(self, name):
        folders = self.find_folders(name)

        folders_len = len(folders)
        if folders_len != 1:
            if folders_len == 0:
                err_messaege = 'No folder "%s" found.' % name
            else:
                err_messaege = 'Too many folders named "%s" found.' % name

            raise ValueError(err_messaege)
        return folders[0]
