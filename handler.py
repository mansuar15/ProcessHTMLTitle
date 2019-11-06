import requests
from bs4 import BeautifulSoup

def getTitle(event, context):
    try:
        r=requests.get(event)
        soup = BeautifulSoup(r.text, "html.parser")
    except:
        return 'error'
    return soup.title.text