from __future__ import print_function
import os.path, os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas, xlwt, pickle

wb = xlwt.Workbook()
path = 'Gform.csv'
sheet1 = wb.add_sheet('G-Form')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
# link = input('\nEnter or PASTE... Google SpreadSheet link : ')
# link = 'https://docs.google.com/spreadsheets/d/15hXurtpkhacOSmFcb_Jt0ojl_j2D2YyjO3tv7AAFtxs/edit#gid=768182159'
link = 'https://docs.google.com/spreadsheets/d/1DW3OHq9u3mDIUKsngMLQkU-47-QKAWrYylpWZ2YFt8M/edit#gid=66752240'
SAMPLE_SPREADSHEET_ID = link.split('/')[5]

# SAMPLE_SPREADSHEET_ID = '1DW3OHq9u3mDIUKsngMLQkU-47-QKAWrYylpWZ2YFt8M'
# SAMPLE_SPREADSHEET_ID = '1FgZbO7R0ZKFKsmxml-cUosHcqAn-p5W-dxRpiTpRVhw'
SAMPLE_SPREADSHEET_ID = '1FAIpQLScF17GULOP1OxI9MHbn0nsIre71hIeCKR8mLyvmwhMXLiyTuA'
SAMPLE_RANGE_NAME = 'A:ZZ'

credentials = 'credentials.json'
credentials_xlsx = "xlsx.xlsx"

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials , SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(values)
        for r, row in enumerate(values):
            for c, column in enumerate(row):
                sheet1.write(int(r), int(c), column)

if __name__ == '__main__':
    main()
    wb.save(path)
    os.startfile(path)

#     pandas.read_json(credentials).to_excel(credentials_xlsx)
#     os.startfile(credentials_xlsx)
