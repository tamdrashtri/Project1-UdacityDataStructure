"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

"""

# turn into integers

time = {}

for number in calls:
  if number[0] in time:
    time[number[0]] += int(number[3])
  else:
    time[number[0]] = int(number[3])
  if number[1] in time:
    time[number[1]] += int(number[3])
  else:
    time[number[1]] = int(number[3])

# since it's dictionary we use key = time.get
longest_time = max(time, key = time.get)

print(f'{longest_time} spent the longest time, {time[longest_time]} seconds, on the phone during September 2016')