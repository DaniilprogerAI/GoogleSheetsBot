import gspread
from google.oauth2.service_account import Credentials

def write_to_sheets(data):
    creds = Credentials.from_service_account_file("credentials.json")
    client = gspread.authorize(creds)
    sheet = client.open("MyDataSheet").sheet1
    sheet.clear()
    for i, item in enumerate(data, start=1):
        sheet.update_cell(i, 1, item)
