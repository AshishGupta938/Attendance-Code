import outside_google
import gspread
from oauth2client.service_account import ServiceAccountCredentials

array = list(())
for dictionary in outside_google.list_of_hashes:
    timestamp_dict = dictionary["Timestamp"]
    name_dict = dictionary["Name?"]
    inout_dict = dictionary["Hours (integer)?"]
    inout_dict = str(inout_dict)
    final_string_dict = timestamp_dict + "flup" + name_dict + "flup" + inout_dict
    array.append(final_string_dict)

mydict = {
  "Abhijit": 0,
  "Alex": 0,
  "Amelia": 0,
  "Amr": 0,
  "Ananya": 0,
  "Andrew": 0,
  "Ankith": 0,
  "Ashish": 0,
  "Ashwin": 0,
  "Cole": 0,
  "David": 0,
  "Harshul": 0,
  "Jacob": 0,
  "Kunal": 0,
  "Lahari": 0,
  "Manas": 0,
  "Mohit": 0,
  "Nikhil": 0,
  "Pradnesh": 0,
  "Rishi": 0,
  "Shriyansh": 0,
  "Somya": 0,
  "Sriram": 0,
  "Sriya": 0,
  "Sushrit": 0,
  "Varun": 0,
  "Vidisha": 0,
  "Zaineb": 0

  }

for i in range(0,len(array)):
  drop, name_i, hour_i = array[i].split("flup")
  hour_i = int(hour_i)
  mydict[name_i] += (hour_i / 2.0)

def step(mydict):
  return mydict
