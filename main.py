from DriveAPI import Drive
from GoogleAPI import GoogleAPI
from SheetsAPI import SheetsAPI
import os
try:
    os.remove('tokendrive.pickle')

except:
    pass
try:
    os.remove('tokensheets.pickle')
except:
    pass
# SPREADSHEET_ID = "1UnFOh4in0gWz9_qmsoW16Pl2QsJDi04CPgLrn9vGvZw"
#
# sheets = SheetsAPI(SPREADSHEET_ID)
# a = sheets.getStudentList()
# print(a)
drive = Drive()
drive.createFolderTree("Bài tập tuần 02")
#success
# items = drive.getFilesList()
#
# for i in items:
#     print('with name: {} and id: {}'.format(i.get('name'), i.get('id')))
# #success

#drive.createFolder(name = "Dũng siêu siêu đẹp trai !!!")
#success

# list = drive.searchFiles(name="Dũng siêu siêu đẹp trai !!!")
#
# for file in list:
#     drive.downloadFile(file)
# #success
# drive.createFolderTree(name='Bài tập tuần 2')
