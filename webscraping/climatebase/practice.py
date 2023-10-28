from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


driver = webdriver.Chrome()

# Define the URL you want to scrape
url = 'https://app.dealroom.co/lists/33849'

# Open the webpage
driver.get(url)
time.sleep(30)

page_source = driver.page_source
captured_content = list()
 # Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')
 # Find and extract the desired elements (adjust the selector as needed)
html_cards = soup.find_all('div', class_='table-list-item')
# cards.append(html_cards)
# print(cards)

 # Check if we've already captured this content
for index,card in enumerate(html_cards):
    title=card.find('div',class_='list_card__title').text.strip()
    image=card.find('img',class_='responsive-img').text.strip()
    image=image['src']
    company_name=(card.find('a',class_='entity-name__name-text')).text.strip()
    tagline=(card.find('div',class_="type-element type-element--p6 entity-name__tagline no-wrap")).text.strip()
    ranking_bar=(card.find('div',class_="ranking-bar-legend")).text.strip()
    # //*[@id="list-map-list"]/div/div[2]/div/div[1]/div[2]/div[2]/div/ul[1]/li/a
    # people=card.select_one('div[type="people"]').text.strip()
    # people=card.select_one('div[type="people"]').text.strip()
    # team_numbers=card.find_all('div',class_='MetadataInfo__MetadataInfoStyle-hif7kv-1 hJCqBA list_card__metadata-item')[-1]
    description=card.find('div',class_='list_card__description').text.strip()
    
    if(card.find('div',class_='list_card__tag')):
        type=card.find('div',class_='list_card__tag').text
    else:
        type=''
    

    captured_content.append({
        'Sr No.':index,
        'title': title,
        'type': type,
        'location':type,
        'people':type,
        'description': description
        })



  # Close the WebDriver
driver.quit()
field_names = ['Sr No.','title', 'type','location','people','description']
with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(captured_content)
csvfile.close()