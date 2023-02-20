from requests import get
from selenium import webdriver
from bs4 import BeautifulSoup

def get_page_count(keyword):
    browser = webdriver.Chrome()
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source,'html.parser')
    pagination = soup.find('nav',class_='ecydgvn0')
    if pagination == None:
        return 1
    pages=pagination.find_all("div",recursive=False)
    print(len(pages))
    
get_page_count('nest')

def extract_indeed_jobs(keyword):
    browser = webdriver.Chrome()
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    results=[]
    soup=BeautifulSoup(browser.page_source,'html.parser')
    job_list = soup.find("ul", class_="jobsearch-ResultsList")

    jobs = job_list.find_all('li', recursive=False) 
    #바로 아래에 있는 것만 검색하고 그 자식요소는 검색하지 않는다

    for job in jobs:
        zone=job.find("div",class_='mosaic-zone')
        if zone == None:
            anchor = job.select_one('h2 a')
            title=anchor['aria-label']
            link=anchor['href']
            company=job.find('span',class_='companyName')
            location=job.find('div',class_='companyLocation')
            job_data={
                'link':f'https://kr.indeed.com{link}',
                'company':company.string,
                'location':location.string,
                'position':title
            }
            results.append(job_data)
    for result in results:
        print(result,'\n///////\n')        
    
while (True):
    pass