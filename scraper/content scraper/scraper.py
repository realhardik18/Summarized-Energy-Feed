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

for articel in articels[1:3]:
    driver.get(articel)
    time.sleep(5)
    content=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[4]/main/div/div/div/div/article/div/div[3]/div[1]/div[1]')
    filename=f"{articel[len(articel)-articel[::-1].index('/'):]}.txt"
    with open(filename,'w+') as file:
        file.write('content')
    with open('data.json','r') as readFile:
        data=json.load(readFile)
    #work on adding data to the json file
    


