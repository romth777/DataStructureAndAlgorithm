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
from collections import defaultdict
phone_time = defaultdict(int)
for item in calls:
    phone_time[item[0]] += int(item[3])
    phone_time[item[1]] += int(item[3])

max_val = 0
max_key = ""
for key, val in phone_time.items():
    if val > max_val:
        max_val = val
        max_key = key
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, max_val))
