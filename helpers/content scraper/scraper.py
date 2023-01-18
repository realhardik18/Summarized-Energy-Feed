#THIS SCRIPT SCRAPES ALL THE CONTENT FROM THE BLOG POSTS AND SAVES THEM IN DATA.JSON
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import json

options = Options()
#options.headless = True
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()), options=options)

with open('scraper\crawler\links.txt','r') as file:
    articels=file.readlines()

i=0
for articel in articels:
    try:
        driver.get(articel)
        time.sleep(5)
        content=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[4]/main/div/div/div/div/article/div/div[3]/div[1]/div[1]').text
        authors=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[4]/main/div/div/div/div/article/div/div[3]/div[2]/div[1]')
        authors=authors.find_elements(By.CLASS_NAME,'field__item')
        #publish_date=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[4]/main/div/div/div/div/article/div/div[3]/div[1]/div[1]/p[12]/em').text
        authors_data=list()
        for author in authors:
            authors_data.append(author.text)
        authors_data=list(set(authors_data))
        name=articel[len(articel)-articel[::-1].index('/'):]
        with open(f'scraper\content scraper\content\{i}.txt','w') as file:
            file.write(content)
        with open('scraper\content scraper\data.json','r') as readFile:
            data=json.load(readFile)
        data['data'].append(
            {
                "name":name,
                "authors":authors_data

            }
        )
        with open('scraper\content scraper\data.json','w+') as outFile:
            json.dump(data,outFile)
        i+=1
    except Exception as e:
        pass


