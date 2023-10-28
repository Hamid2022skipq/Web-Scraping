from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import csv
driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://www.linkedin.com/jobs/search/?currentJobId=3674610800&f_C=14074&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=3674610800%2C3742539028%2C3742537172%2C3736858856%2C3743126137%2C3670987672%2C3676611127%2C3734550924%2C3743121721'
driver.get(url)
sign_in_button = driver.find_element(
    "css selector", ".nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()
username = 'faltorecycle@gmail.com'
password = 'Django,123'

driver.find_element(By.ID, 'username').send_keys(username)
time.sleep(3)
driver.find_element(By.ID, 'password').send_keys(password)
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'btn__primary--large').click()
time.sleep(30)
# driver.find_element(By.CLASS_NAME, 'artdeco-button__icon').click()
print('Logged In Successfully')
time.sleep(100)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
job_listings = soup.find_all('div', class_='base-card')
job_data = []
# Iterate through each job listing and extract relevant information
for index,job in enumerate(job_listings):
    image = job.find('img', class_='artdeco-entity-image artdeco-entity-image--square-4 lazy-loaded')
    image_url= image['src'] if image else '_'
    job1 = job.find('h3', class_='base-search-card__title')
    job_name=job1.text.strip() if job1 else '_'
    loca = job.find('span', class_='job-search-card__location')
    location= loca.text.strip() if loca else '_'
    sal = job.find('span', class_='job-search-card__salary-info')
    salary= sal.text.strip() if sal else '_'
    title = job.find('h3', class_='base-search-card__title')
    card_title= title.text.strip() if title else '_'
    url = job.find('a', class_='base-card__full-link')
    anchor_url = url['href'] if url else '_'
    div_element1 = job.find('h4', class_='base-search-card__subtitle')
    company=div_element1.find('a',class_='hidden-nested-link')
    company_name = company.text.strip() if company else '_'
    company_url = company['href'] if company else '_'
    benefit=job.find('span', class_='result-benefits__text')
    benefits = benefit.text.strip() if benefit else '_'
    posted=job.find('time', class_='job-search-card__listdate')
    posteds = posted.text.strip() if posted else '_'
    data={
    'Company Name':company_name,
    'Company url':company_url,
    "Job Title":job_name,
    'Image Path':image_url,
    'Location':location,
    'Job page link':anchor_url,
    'Hiring':benefits,
    'Published Date':posteds,
    }
    job_data.append(data)
print(len(job_data))
field_names = ['Company Name','Job Title','Published','Location','Hiring','Company url','Job page link','Image Path',]
with open('Dematic_jobs1.csv', 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(job_data)
csvfile.close()