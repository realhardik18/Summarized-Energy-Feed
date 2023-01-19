import requests
from creds import ApiHost,ApiKey,ApiUrl
import time

def summarizeContent(url):
    payload = {
        "url": url,
        "min_length": 250,
        "max_length": 300,
        "is_detailed": False
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": ApiKey,
        "X-RapidAPI-Host": ApiHost
    }

    response = requests.request("POST", ApiUrl, json=payload, headers=headers)
    return response.text

with open('helpers\crawler\links.txt','r') as file:
    links=file.readlines()

links=[link.strip('\n') for link in links]

i=0
for link in links:
    try:
        SummarizedText=summarizeContent(link)
        if '"messages":"The API is unreachable, please contact the API provider", "info": "Your Client (working) ---> Gateway (working) ---> API (not working)' not in SummarizedText:
            with open(fr'helpers\content summarization\summarizedContent\{i}.json','w') as outFile:
                outFile.write(SummarizedText)
            print(f'summarized doc {i} || {time.ctime()}')
            i+=1
            time.sleep(100)
        else:
            print(f'failed || {time.ctime()}')
    except Exception as e:
        print(f'failed || {time.ctime()}')

