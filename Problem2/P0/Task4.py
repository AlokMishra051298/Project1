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
callers=set()
receivers=set()
for x in calls:
    callers.add(x[0])
    receivers.add(x[1])
for x in texts:
    receivers.add(x[0])
    receivers.add(x[1])
tele=callers-receivers
print("These numbers could be telemarketers: ")
print(len(tele))
tele=sorted(tele)
for x in tele:
    print(x)
