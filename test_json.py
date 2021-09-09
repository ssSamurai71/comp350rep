import json
import boto3

#json.loads
#json.dumps

with open('test.json') as f:
    data=json.load(f)

#print(type(data['Messages']))
#print(len(data['Messages']))
body=data['Messages'][0]['Body']

#print(body)

stringvar=json.dumps(body,indent=2)

#print(stringvar)

x= stringvar.split()

y=x[2]

z=y.split('/')

#print(z)
z.pop(0)
z.pop(0)
#print(z)

var='"'
for each in z:
    if('submissions'== each):
        print()
    else: 
        var += ('/'+ each)

print(var)