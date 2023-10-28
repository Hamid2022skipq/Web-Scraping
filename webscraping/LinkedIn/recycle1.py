from bs4 import BeautifulSoup
import re


# soup = BeautifulSoup(, 'html.parser')
soup=True
# t-24 t-bold job-details-jobs-unified-top-card__job-title

# Extract the job description
job_description =job_description = soup.find('h2', class_='text-heading-large').find_next('ul').get_text(strip=True)
# 
# Extract education information (with a check for existence)
tags = soup.find_all('strong')
education = "Not found"
for tag in tags:
    if "Education:" in tag.text:
        education = tag.find_next('ul').text.strip()
        break



# Extract knowledge and experience (with a check for existence)
knowledge_experience = "Not found"
for tag in tags:
    if "Knowledge and Experience:" in tag.text:
        knowledge_experience = tag.find_next('ul').text.strip()
        break


skills = "Not found"
for tag in tags:
    if "Skills:" in tag.text:
        skills = tag.find_next('ul').text.strip()
        break
print('Job Description : ',job_description)
print("Education:", education)
print("Knowledge and Experience:", knowledge_experience)
print("Skills:", skills)
