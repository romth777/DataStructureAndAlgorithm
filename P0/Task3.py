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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
import re

# partA
rets = set()
p = re.compile(r'\(080\)')

cnt_b2any = 0
cnt_b2b = 0
for item in calls:
    flg_call = False
    flg_rev = False
    if p.match(item[0]) is not None:
        if re.compile(r'[0-9]{4}').match(item[1]) is not None:
            rets.add(item[1][0:4])
        else:
            if re.compile(r'\([0-9]{3}\)').match(item[1]) is not None:
                rets.add(item[1][1:4])
            elif re.compile(r'\([0-9]{4}\)').match(item[1]) is not None:
                rets.add(item[1][1:5])
            elif re.compile(r'\([0-9]{5}\)').match(item[1]) is not None:
                rets.add(item[1][1:6])
        flg_call = True
    if p.match(item[1]) is not None:
        flg_rev = True

    if flg_call:
        if flg_rev:
            cnt_b2b += 1
            cnt_b2any += 1
        else:
            cnt_b2any += 1
rets = sorted(rets)

print("The numbers called by people in Bangalore have codes:")
for item in rets:
    print(item)

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(cnt_b2b / cnt_b2any * 100, 2)))

