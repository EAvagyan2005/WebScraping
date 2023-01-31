from bs4 import BeautifulSoup
import requests
import msvcrt
import time
DEL_CHARS = ' \n\r'
my_skills = list()



def get_jobs():
    html_file = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
    html_text = html_file.text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, post in enumerate(posts):
        job_name = post.find('header', class_="clearfix").h2.a.text.strip(DEL_CHARS)
        job_company = post.find('h3', class_="joblist-comp-name").contents[0].text.strip(DEL_CHARS).upper()
        job_skills = post.find('span', class_="srp-skills").text.strip(DEL_CHARS).replace(' ', '').replace(',', ' ').title()
        job_link = post.find('header', class_="clearfix").h2.a['href']
        for i in my_skills:
            if i.title() in job_skills.split():
                with open(f'{index}.txt', 'w') as f:
                    f.write(f"""name:     {job_name}
company:  {job_company}
skills:   {job_skills}
more info:{job_link}
""")
                print(f"""
            name:      {job_name}
            company:   {job_company}
            skills:    {job_skills}
            more info: {job_link}
            """)


if __name__ == '__main__':
    aborted = False
    my_skills = input("enter your skills: ").replace(',', ' ').split()
    while not aborted:
        get_jobs()
        time.sleep(10)
        if msvcrt.kbhit() and msvcrt.getch() == chr(27):
            aborted = False


