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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
phones=set()
for x in texts:
    phones.add(x[0])
    phones.add(x[1])
for x in calls:
    phones.add(x[0])
    phones.add(x[1])
#print(phones.count('98459 44682'))
print("There are",len(phones),"different telephone numbers in the records.")
