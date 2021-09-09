#Written by Jose Cahue and Arthur Hui
import json
import boto3

#json.loads
#json.dumps

#open the json file
with open('test.json') as f:
    data=json.load(f)

#First we checked where need the type of message and how long the message from the JSON file given.
#This step was a sanity check since we had to pull the file path from the JSON and it was stored in body.
#print(type(data['Messages']))
#print(len(data['Messages']))
body=data['Messages'][0]['Body']

#Sanity check so we know we are printing the line we need.
#print(body)

#use json.dumps to get to become a python dictionary we was can parse
stringvar=json.dumps(body,indent=2)

#another sanity check, printing stringvar allowed us to confirm that we were narrowing what we are looking from the dump.
#print(stringvar)

#we then split the dictionary to manipulate the different sections of it
x=stringvar.split()

#we removed some sanity checks that were commented but from them we found that the 3 index of the dictionary is what we need. (python indexes from so we use 2 to access the third index)
y=x[2]

#we split the that part up by / since the file paths use the / to seperate each name
z=y.split('/')

#The prints are sanity checks that allow us to know that we remove redundent 2 redundent parts of the file path since we are already in the area of the bucket we need to be in. 
#the pops are to get rid of the redundant file path parts in the dictionary.
#print(z)
z.pop(0)
z.pop(0)
#print(z)

#This part is were we rebuild the string and print it for a sanity check.
#We start with a quote to prevent issues in when we finish it in the actual lambda side of aws and becasue the last thing part in the dictionary has a " at the end.
#The " is important for the backend to parse through it.
var='"'
for each in z:
    if('submissions'== each): #here is just a sanity check that will print once 
        print()
    else: 
        var += ('/'+ each) #just add / whatever was in the dictionary 

print(var) #final string that would be passed onto the backend.
