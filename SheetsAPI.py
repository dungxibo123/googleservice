from GoogleAPI import GoogleAPI

class SheetsAPI:
    def __init__(self):
        api = GoogleAPI('sheets')
        self.service = api.service
    def getSheet(self,id):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id).execute()
        return result
    def getListOfStudent(self,id,amount = 10):
        # Lấy số học sinh theo số lượng học sinh có trong sheet, tất cả nên được ghi ở bảng có tên class để HTTP Request gửi đúng link =)) thanks
        sheet = self.service.spreadsheets()
        range_names = [
        "A2:A{}".format(amount + 1)
        ]
        result = sheet.values().batchGet(
            spreadsheetId=id, ranges=range_names).execute()
        ranges = result.get('valueRanges', [])
        student = []
        for box in ranges:
            student.append(box.get('string_value'))
        print('{0} ranges retrieved.'.format(len(ranges)))
