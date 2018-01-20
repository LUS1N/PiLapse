from google_api.uploaders.base import BaseUploader 

class Youtube(BaseUploader):

    def __init__(self, appName):
        BaseUploader.__init__(self, appName, "youtube")
        print(self.credentials.value)
    

    