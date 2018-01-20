from google_api.uploaders.base import BaseUploader

class Youtube(BaseUploader):
    """Class handling uploading videos yo Youtube
    """

    def __init__(self, appName):
        BaseUploader.__init__(self, appName, "youtube")

    def upload_video(self, path, name, description=None, tags=None, category=None, privacy_status='public'):
        """ Uploads a video file to youtube
        Returns:
            Response from the api
        """
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
