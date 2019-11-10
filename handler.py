import requests
from bs4 import BeautifulSoup
import boto3

def getTitle(event, context):
    try:
        r=requests.get(event)
        soup = BeautifulSoup(r.text, "html.parser")
    except:
        return 'error'
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    #s3 = boto3.resource('s3')
    #response = s3.list_buckets()
    #bucket = s3.Bucket('python-http-get-title-bucket')
    s=s3.put_object(Bucket='python-http-get-title-bucket',Key=soup.title.text,Body=r.text,ACL='public-read-write')

    # Output the bucket names:
    #print('Existing buckets:')
    #for bucket in response['Buckets']:
        #return f'  {bucket["Name"]}'
    return soup.title.text, s