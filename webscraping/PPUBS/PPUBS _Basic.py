from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


driver = webdriver.Chrome()

url = 'https://ppubs.uspto.gov/pubwebapp/static/pages/ppubsbasic.html'
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