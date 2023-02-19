from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs=soup.find_all('table', id_="jobsboard")
        for job_table in jobs:
            job_posts = job_table.find_all('tr')
        #     job_posts.pop(-1)
        #     for post in job_posts:
        #         anchors = post.find_all('a')
        #         anchor = anchors[1]
        #         link=anchor['href']
        #         company,kind,region=anchor.find_all('span',class_='company')
        #         title = anchor.find('span',class_='title')
        #         print(company,kind,region,title)
        #         print("///////////")
    else:
        print("Can't get jobs.")

extract_jobs("rust")