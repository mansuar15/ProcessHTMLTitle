import requests
from bs4 import BeautifulSoup

def getTitle(event, context):
    r=requests.get(event)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.title.text