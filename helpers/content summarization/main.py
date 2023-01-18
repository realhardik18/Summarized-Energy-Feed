import requests
from creds import ApiKey,ApiHost,ApiUrl
import os 

def Summarize(content):
    payload = {
        "text": content,
        "num_sentences": 10
    }
    headers = {
        "content-type": "application/json",
        "Key": ApiKey,
        "Host": ApiHost
    }

    response = requests.request("POST", ApiUrl, json=payload, headers=headers)

    return response.text

for file in os.listdir('helpers\content scraper\content'):
    with open(fr'helpers\content scraper\content\{file}') as contentFile:
        summarizedContent=Summarize(contentFile.read())
    #with open('helpers\content summarization\summarizedContent')
    #work form here
    #make summazrized content files and then website part
    #gn