import gspread
from google.oauth2.service_account import Credentials

# 🔹 Добавляем нужные области доступа (scopes)
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def write_to_sheets(data):
    creds = Credentials.from_service_account_file("storied-sound-475506-f4-9e44ff711275.json", scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open("MyDataSheet").sheet1
    sheet.clear()
    for i, item in enumerate(data, start=1):
        sheet.update_cell(i, 1, item)
