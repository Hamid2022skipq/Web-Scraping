from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://ppubs.uspto.gov/pubwebapp/static/pages/ppubsbasic.html'
driver.get(url)
time.sleep(90)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# scraping data
table1 = soup.find('tbody') 
table = table1.find_all('tr') 
data_list = []
for row in table:
    td_elements = row.find_all('td')
    patent_number = td_elements[1].text
    pdf_link = td_elements[2].find('a')['href']
    title = td_elements[3].text
    inventor = td_elements[4].text
    publication_date = td_elements[5].text
    page_count = td_elements[6].text
    data_dict = {
        'Patent number': patent_number,
        'Title': title,
        'PDF link':pdf_link,
        'Inventor name': inventor,
        'Date': publication_date,
        'Page count': page_count
    }
    data_list.append(data_dict)
print(len(data_list))


# Saving Data into Csv file
field_names = ['Patent number', 'Title','Inventor name','Date','Page count','PDF link']
with open('PPUBS_Basic.csv', 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(data_list)
csvfile.close()
