from bs4 import BeautifulSoup
import requests
import time
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
soup=BeautifulSoup(html_text,'html.parser')
# html_card=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
html_card=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
# print('Please enter one unfimilar Skill')
# unfimilar=input('>')
# print(unfimilar)

def func():
    for card in (html_card):
        posted_date=card.find('span',class_='sim-posted').text.strip()
        if 'few' in posted_date: 
            company=card.find('h3',class_='joblist-comp-name').text.strip()
            skill=card.find('span',class_='srp-skills').text.replace(' ','').strip()
            des=card.find('ul',class_='list-job-dtl clearfix').text.strip()
            job_description = card.ul.find('li').text.replace('card_travel','').strip()
            job_more_info = card.header.h2.a['href']
        
        # If the tag exists, extract the text
            # if job_description_tag:
            #     job_description = job_description_tag
            # else:
            #     job_description = None
            # if unfimilar not in skill:
            with open(f'post/index.txt','a') as f:
                f.write(f'____________________________*____________________________________*_________________________\n')
                f.write(f' \n')
                f.write(f'Company Name : ,{company}\n')
                f.write(f'Required Skills : ,{skill}\n')
                f.write(f'Job required experience : ,{job_description}\n')
                f.write(f'More Info : ,{job_more_info}\n')
                f.write(f' \n')
    print(f'File Saved Sucessfully index.txt')
if __name__== '__main__':
    while True:
        func()
        waiting_time=10
        print(f'Waiting for {waiting_time} Minutes...')
        time.sleep(waiting_time*60)
