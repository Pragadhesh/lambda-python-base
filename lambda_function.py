# This is a sample lambda function
import requests
from urllib3.util.request import set_file_position

def lambda_handler(event,context):
    print(event)
    print(context)
    print ("This is the event")
    value = event['id']
    result = requests.get("https://api.spacexdata.com/v3/launches")
    data = result.json()
    try:
        launch_details = data[value-1]
    except:
        launch_details = "Not a valid id"
    print(launch_details)
    # TODO implement
    return {
        'statusCode': 200,
        'body': launch_details
    }

'''
If we need to test the function locally either we can use main block and pass values
or we can test using the following method 
python -c "import lambda_function; print (lambda_function.lambda_handler({'id':100},{'context':00}))" - double quotes for windows
linux - single quotes
'''

#if __name__=="__main__":
    #event = 10
    #lambda_handler(event,9999)
'''
Build command - docker build -t lambda-base .
Run command - docker container run -p 9000:8080 lambda-base
Validation - curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"id":10}'
'''