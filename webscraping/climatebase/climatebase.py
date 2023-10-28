from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


driver = webdriver.Chrome()

# Define the URL you want to scrape
# url = 'https://climatebase.org/climate-tech-companies?l=USA&q=&p=9&hiring=no'
url = 'https://climatebase.org/climate-tech-companies?l=USA&q=&sectors=Advocacy+or+Policy&sectors=Buildings&sectors=Carbon+Removal+Tech&sectors=Climate+Adaptation&sectors=Coastal+%26+Ocean+Sinks&sectors=Energy&sectors=Materials+%26+Manufacturing&sectors=Media+%26+Journalism&sectors=Other&sectors=Research+%26+Education&organization_size=11-50&organization_size=51-100&organization_size=101-250&organization_size=251-500&organization_size=501-1000&organization_size=1001-5000&organization_size=5001-10000&organization_size=10000+%2B&p=0&hiring=no'
# Open the webpage
driver.get(url)
time.sleep(60)

page_source = driver.page_source
captured_content = list()
soup = BeautifulSoup(page_source, 'html.parser')
html_cards = soup.find_all('div', class_='list_card__main')
for index,card in enumerate(html_cards):
    title1=card.find('div',class_='list_card__title')
    if (title1):
        title=title1.text.strip()
    else:
        people='-'

    loc=card.find('div',class_='list_card__metadata-item')
    if (loc):
        location=loc.text.strip()
    else:
        location='-'

    peopl=card.select_one('div[type="people"]')
    if (peopl):
        people=peopl.text.strip()
    else:
        people='-'
    
    desc= card.find('div',class_='list_card__description')
    if (desc):
        description=desc.text.strip()
    else:
        description='-'
    
    tags=card.find('div',class_='list_card__tag')
    if(tags):
        type=tags.text
    elif(card.find('div',class_='list_card__tags')):
        type=card.find('div',class_='list_card__tag').text
    else:
        type='-'
    captured_content.append({
        'title': title,
        'type': type,
        'location': location,
        'people': people,
        'description': description
        })

  # Close the WebDriver
driver.quit()
# field_names = ['title', 'type','location','people','description']
# # with open('climatebase1.csv', 'a') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = field_names)
#     writer.writeheader()
#     writer.writerows(captured_content)
# csvfile.close()