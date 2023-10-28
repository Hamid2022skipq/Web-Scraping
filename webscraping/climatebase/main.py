from bs4 import BeautifulSoup
with open('hello.html','r') as file:
    content=file.read()
    # print(content)
    soup=BeautifulSoup(content,'lxml')
    # html_tag=soup.find('h1')
    # html_tag=soup.find_all('h1')
    # print(html_tag)
    # for tag in html_tag:
    #     print(tag.text)
    html_card=soup.find_all('div',class_='card')
    for card_content in html_card:
        course_name=card_content.h1.text
        course_price=card_content.button.text.split()[-1]
        print("Course Name : ",course_name, '|| Course Price : ', course_price)
