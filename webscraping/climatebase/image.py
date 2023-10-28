from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()

# Define the URL you want to scrape
url = 'https://climatebase.org/climate-tech-companies?l=USA&q=&p=9&hiring=no'   # Replace with the actual URL

# Open the webpage
driver.get(url)

# Use JavaScript to extract CSS file URLs from the loaded webpage
css_file_urls = driver.execute_script("""
    var cssFileUrls = [];
    var links = document.querySelectorAll('link[rel="stylesheet"]');
    for (var i = 0; i < links.length; i++) {
        cssFileUrls.push(links[i].href);
    }
    return cssFileUrls;
""")

# Download and parse the CSS files to extract background image URLs
background_image_pattern = re.compile(r'url\((.*?)\)')

background_images = set()

for css_url in css_file_urls:
    css_response = requests.get(css_url)
    if css_response.status_code == 200:
        css_content = css_response.text
        matches = background_image_pattern.findall(css_content)
        if matches:
            background_images.update(matches)


for url in background_images:
    print("Background Image URL:", url)


driver.quit()
