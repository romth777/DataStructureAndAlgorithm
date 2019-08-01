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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

record0 = texts[0]
print("First record of texts, {} texts {} at time {}".format(record0[0], record0[1], record0[2]))

record1 = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(record1[0], record1[1], record1[2], record1[3]))
