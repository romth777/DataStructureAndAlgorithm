"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

send_texts = set()
receive_texts = set()
for item in texts:
    send_texts.add(item[0])
    receive_texts.add(item[1])

send_calls = set()
receive_calls = set()
for item in calls:
    send_calls.add(item[0])
    receive_calls.add(item[1])

print("These numbers could be telemarketers: ")
for_telemarketers = send_calls.difference(send_texts, receive_texts, receive_calls)
for item in for_telemarketers:
    print(item)