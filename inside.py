import googleTest
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
array = list(())
for dictionary in googleTest.list_of_hashes:
    timestamp_dict = dictionary["Timestamp"]
    name_dict = dictionary["Name?"]
    inout_dict = dictionary["In or Out?"]
    final_string_dict = timestamp_dict + "flup" + name_dict + "flup" + inout_dict
    array.append(final_string_dict)

numlines = len(array)
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

names = list(("Abhijit", "Alex", "Amelia", "Amr", "Ananya", "Andrew", "Ankith", "Ashish", "Ashwin", "Cole", "David", "Harshul", "Jacob", "Kunal", "Lahari", "Manas", "Mohit", "Nikhil", "Pradnesh", "Rishi", "Shriyansh", "Somya", "Sriram", "Sriya", "Sushrit", "Varun", "Vidisha", "Zaineb"))
hours = list((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
lastin = list((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
status = list(("Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out", "Out"))
first_in = list(())
last_out = list(())
for i in range(0,len(names)):
  first_in.append(0)
  last_out.append(0)

def reset():
  global lastin
  global status
  global first_in
  global last_out
  lastin = list(())
  status = list(())
  first_in = list(())
  last_out = list(())
  for i in range(0, len(names)):
    lastin.append(0)
    status.append("Out")
    first_in.append(0)
    last_out.append(0)

def get_string_data(string):
  timestamp, name, status = string.split("flup")
  date, time = timestamp.split(" ")
  month, day, year = date.split("/")
  month = int(month)
  day = int(day)
  hours, minutes, seconds = time.split(":")
  hours = int(hours)
  minutes = int(minutes)
  hours += (minutes / 60.0)
  if month > 1: day += 31
  if month > 2: day += 28
  if month > 3: day += 31
  if month > 4: day += 30
  if month > 5: day += 31
  if month > 6: day += 30
  if month > 7: day += 31
  if month > 8: day += 31
  if month > 9: day += 30
  if month > 10: day += 31
  if month > 11: day += 30
  index = names.index(name)
  first = first_in[index]
  last = last_out[index]
  output = list((day, hours, name, status, first, last, index))
  return output

#find each person's IN and their OUT on any given day
#every day, check peoples' INs and OUTs

#given the day's lines
#check for each name
#check for IN or OUT
#if IN, find earliest one
#if OUT, find latest one

final_sum = 0

current_day = 1
last_day = get_string_data(array[-1])[0]

for current_day in range(1,(last_day+1)):

  for line in range(0,len(array)):
    #per line
    if current_day == get_string_data(array[line])[0]:
      #checks if it is the right day
      for name in names:
        #per name
        if get_string_data(array[line])[2] == name:
          #checks if it is the right name
          if get_string_data(array[line])[3] == "In" or get_string_data(array[line])[3] == """In
""":
            #checks if the status is IN
            if get_string_data(array[line])[4] == 0:
              #checks if the first_in is 0
              first_in[get_string_data(array[line])[6]] = get_string_data(array[line])[1]
            elif get_string_data(array[line])[4] >= get_string_data(array[line])[1]:
              #checks if the first_in is later than the time
              first_in[get_string_data(array[line])[6]] = get_string_data(array[line])[1]
            else: pass
          elif get_string_data(array[line])[3] == "Out" or get_string_data(array[line])[3] == """Out
""":
            #checks if the status is OUT
            if get_string_data(array[line])[5] == 0:
              last_out[get_string_data(array[line])[6]] = get_string_data(array[line])[1]
            elif get_string_data(array[line])[5] <= get_string_data(array[line])[1]:
              last_out[get_string_data(array[line])[6]] = get_string_data(array[line])[1]
            else: pass
          else:
            print ("ERROR 01")

    else:
      pass

  max_list = list(())

  for name in names:
    ind = names.index(name)
    if last_out[ind] == 0 and first_in[ind] != 0:
      differ = 1.0
    elif first_in[ind] == 0 and last_out[ind] != 0:
      differ = 1.0
    elif first_in[ind] == 0 and last_out[ind] == 0:
      differ = 0.0
    elif first_in[ind] != 0 and last_out[ind] != 0:
      differ = last_out[ind] - first_in[ind]
    else: print("ERROR 02")
    hours[ind] += differ
    max_list.append(differ)
  max_list_value = np.max(max_list)
  final_sum += max_list_value

  reset()

end_sum = final_sum / 2.0

def updatedict(names,hours,mydict):
  for name in mydict:
    index = names.index(name)
    mydict[name] = hours[index]

updatedict(names, hours, mydict)

def step(mydict):
  return mydict
