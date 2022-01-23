from __future__ import print_function
from googleapiclient.discovery import build
import pandas, xlwt, pickle, os

wb = xlwt.Workbook()
csv = 'Gform.csv'
sheet1 = wb.add_sheet('G-Form')

link = 'https://docs.google.com/spreadsheets/d/1DW3OHq9u3mDIUKsngMLQkU-47-QKAWrYylpWZ2YFt8M/edit#gid=66752240' 
SAMPLE_SPREADSHEET_ID = link.split('/')[5]
SAMPLE_RANGE_NAME = 'A:ZZ'

credentials = 'credentials.json'
pic = 'token.pickle'

with open(pic, 'rb') as token:
    creds = pickle.load(token)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId = SAMPLE_SPREADSHEET_ID, range = SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

print(result)

for r, row in enumerate(values):
    for c, column in enumerate(row):
        sheet1.write(int(r), int(c), column)

wb.save(csv)
os.startfile(csv)
