import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']
url = 'https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/credentials.json'
page = requests.get(url)
with open("credentials.json","+w") as f:
          f.write(page.text)
          f.close()
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
SHEET_ID = '1iGbUayAGHMfJncrIVTRr_ac6GlJPx0BJDpvZEZPpTOE'
try:
    spreadsheet = gc.open_by_key(SHEET_ID)
    print("Successfully syncronized the spreadsheet.")
    print()
except gspread.exceptions.APIError as e:
    print("Error: Could not open the spreadsheet. Reason:", e)

spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet("Sheet1")
rows = worksheet.get_all_records()

os.remove("credentials.json")
