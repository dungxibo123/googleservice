from GoogleAPI import GoogleAPI

class SheetsAPI:
    def __init__(self,id):
        api = GoogleAPI('sheets')
        self.service = api.service
        self.id = id
    def getStudentList(self):
        RANGES = 'Class!A2:A'
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.id,
                                    range=RANGES).execute()
        values = result.get('values', [])
        student = []
        for i in values:
            student.append(i[0])
        return student
