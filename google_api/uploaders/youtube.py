from google_api.uploaders.base import BaseUploader
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload


class Youtube(BaseUploader):

    def __init__(self, appName):
        BaseUploader.__init__(self, appName, "youtube")

    def upload_video(self, path, name, description=None, tags=None, category=None, privacy_status='public', max_retries=10):

        body = {
            'snippet': {
                'title': name,
                'description': description,
                'tags': tags,
                'category':  category
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }

        return self.service.videos().insert(part=",".join(
            body.keys()), body=body, media_body=path).execute()
