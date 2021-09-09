#by Jose Cahue and Arthur Hui
import json

def lambda_handler(event, context):
    #printing event information out to cloudwatch to see what how the metadata looks
    print("EVENT")
    print(event)

    #parse out the JSON from the metadata sent from the S3 bucket using python dictionary notation
    reduceData = event['Records'][0]['s3']['object']['key']
    
    #send that data to the SQS where backend will parse it out
    return {
        'body': {'subdata': reduceData}
    }
