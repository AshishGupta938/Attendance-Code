import outreach, inside, outside
import matplotlib.pyplot as plt
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

for name in mydict:
  mydict[name] = mydict[name] + outreach.step(outreach.mydict)[name] + inside.step(inside.mydict)[name] + outside.step(outside.mydict)[name]

for name in mydict:
  print (str(name) + ": " + str(mydict[name]))


names = list(())
values = list(())
for category in mydict:
  names.append(category)
  values.append(mydict[category])
sorted_lowToHigh = sorted(mydict.values())
sorted_lowToHigh.reverse()

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Attendance Final").sheet1
names_2 = list(("Abhijit", "Alex", "Amelia", "Amr", "Ananya", "Andrew", "Ankith", "Ashish", "Ashwin", "Cole", "David", "Harshul", "Jacob", "Kunal", "Lahari", "Manas", "Mohit", "Nikhil", "Pradnesh", "Rishi", "Shriyansh", "Somya", "Sriram", "Sriya", "Sushrit", "Varun", "Vidisha", "Zaineb"))
for name in names_2:
    num1 = names.index(name) + 2
    num2 = 2
    num3 = mydict[name]
    sheet.update_cell(num1, num2, num3)

for name in names_2:
    num1 = names.index(name) + 2
    num2 = 3
    num3 = inside.mydict[name]
    sheet.update_cell(num1, num2, num3)

for name in names_2:
    num1 = names.index(name) + 2
    num2 = 4
    num3 = (outside.mydict[name] * 2.0)
    sheet.update_cell(num1, num2, num3)

for name in names_2:
    num1 = names.index(name) + 2
    num2 = 5
    num3 = (outreach.mydict[name] / 2.0)
    sheet.update_cell(num1, num2, num3)

sorted_by_value = sorted(mydict.items(), key=lambda kv: kv[1], reverse=True)

name_array = list(())
hours_array = list(())
for tup in sorted_by_value:
    drop_1, main_part = str(tup).split("(")
    main_part, drop_2 = main_part.split(")")
    name_tup, hours_tup = main_part.split(", ")
    hours_tup = float(hours_tup)
    drop_2, name_tup, drop_1 = name_tup.split("'")
    name_array.append(name_tup)
    hours_array.append(hours_tup)

'''
joe = list(('5.0','3.0','7.0'))
phil = list((5.0, 3.0, 7.0))
john = list(())
for i in joe:
    john.append(float(i))
'''

bar_height = inside.end_sum

plt.figure(1, figsize=(20,20))
plt.bar(name_array, hours_array)
plt.xticks(rotation=45)
plt.hlines(bar_height, -2, np.max(30), colors='r', linestyles="dashed")
plt.xlabel("Names")
plt.ylabel("Hours")
plt.show()
