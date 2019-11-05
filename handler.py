import json
import datetime
import requests


def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def anotherFunc(event, context):
    #URL = "http://maps.googleapis.com/maps/api/geocode/json"
    #location = "delhi technological university"
    #PARAMS = {'address':location} 
    #r = requests.get(url = URL, params = PARAMS) 
    r = requests.get('http://www.imdb.com/title/tt0108778/')
    r = requests.get('http://www.google.com/')
    #data = r.json() 

    #latitude = data['results'][0]['geometry']['location']['lat'] 
    #longitude = data['results'][0]['geometry']['location']['lng'] 
    #formatted_address = data['results'][0]['formatted_address'] 
    #print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"%(latitude, longitude,formatted_address))
    body = {
        "message": "Wolol23o!",
        "input": event,
        "elTextoDeR": r.text
    }
    response = {
        "statusCode": 200,
        #"body": json.dumps(body)
        "respuesta": r.text
    }

    return response

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response