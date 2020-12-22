from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = ".config/credentials.json"
SAMPLE_RANGE_NAME = 'A1:E'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1gXzyvkC4TkXTKQ2RFs-DWqMK8MERLFSXCQYZSoHc46M'

def sheet2sheet(request):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        return f'No data found.'
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            return f'{row[0]}'
