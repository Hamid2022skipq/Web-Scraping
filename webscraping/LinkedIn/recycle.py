from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
time.sleep(600)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
div_element = soup.find('div', class_='jobs-search__job-details--container')
print(div_element)
