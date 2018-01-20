from google_api.uploaders.base import BaseUploader 

class Drive(BaseUploader):

    def __init__(self, appName):
        BaseUploader.__init__(self, appName, "drive")

    