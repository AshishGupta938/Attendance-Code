import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Outreach Form (Responses)").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

def output(list_of_hashes):
    return list_of_hashes
