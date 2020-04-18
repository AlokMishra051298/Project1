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
maximum=0
phones={}
for x in calls:
    duration=int(x[3])
    timestamp=x[2].split()
    date=timestamp[0]
    date=date.split('-')
    if date[1]=='09' and date[2]=='2016':
        if(x[0] not in phones):
            phones[x[0]]=duration
        elif(x[0] in phones):
            phones[x[0]]+=duration
        if(x[1] not in phones):
            phones[x[1]]=duration
        elif(x[1] in phones):
            phones[x[1]]+=duration
max_value=0
max_key = ""
for key,value in phones.items():
    if max_value < value:
        max_key= key
        max_value = value
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, max_value))
