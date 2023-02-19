from requests import get
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://kr.indeed.com/jobs?q=python&limit=50")
soup=BeautifulSoup(browser.page_source,'html.parser')
job_list = soup.find("ul", class_="jobsearch-ResultsList")

jobs = job_list.find_all('li', recursive=False)

for job in jobs:
    zone=job.find("div",class_='mosaic-zone')
    if zone == None:
        print('job li')
    else:
        print('mosaic li')
    
while (True):
    pass


