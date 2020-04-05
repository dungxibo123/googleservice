from GoogleAPI import GoogleAPI


class Drive:
    def __init__(self):
        api = GoogleAPI('drive')
        self.service = api.service
    def getFilesList(self):
        service = self.service
        try:
            results = service.files().list(pageSize=10000, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])
            return items
        except Exception as e:
            print("Something went wrong!")
            return None

    def createFolders(self, name = 'folders'):
        metadata = {
            'name': name
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.service.files().create(body=metadata, fields = 'id').execute()
        print ('Folder ID: {}'.format(file.get('id')))
    def insertFileToFolders(self, folder):
        folder_id = folder.get('id')
        pass

    def uploadFiles(self):
        pass
    def downloadFile(self):
        pass
    def getChange(self):
        pass
