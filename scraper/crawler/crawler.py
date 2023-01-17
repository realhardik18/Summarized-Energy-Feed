#THIS SCRIPT GETS ALL THE BLOG LINKS AND SAVES THEM TO links.txt
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

BASE_URL='https://climate.mit.edu'
options = Options()
#options.headless = True
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()), options=options)

for page in range(0,6):
    driver.get(f"https://climate.mit.edu/explainers?sort_bef_combine=created_DESC&sort_by=created&sort_order=DESC&page={page}")
    time.sleep(5)
    posts=driver.find_elements(By.TAG_NAME,'article')
    for post in posts[1:]:
        with open('links.txt','a+') as file:
            file.write(BASE_URL+post.get_attribute('about')+'\n')