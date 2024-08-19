import json

import requests
from bs4 import BeautifulSoup

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story" id="link3">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister fgty" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.find('b').text)
# print(soup.find_all('a'))
# for i in soup.find_all('a'):
#     print(i['class']).

# print(soup.find_all(id='link3'))

# for i in soup.find_all('p' , attrs={'class':'story'}):
#     print(i.text)

# print(soup.p['class'])


# =================================================================
response = requests.get('https://kun.uz/news/category/sport')
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
d = []
for i in soup.find_all('a' ,attrs={'class':'news-page__item l-item'}):
    title = i.find('h3').text
    image_link = i.img['src']
    date = i.p.text
    data = {
        "title": title,
        "image_link": image_link,
        "date": date
    }
    d.append(data)
with open('kun_uz.json', 'w') as outfile:
    json.dump(d, outfile, indent=3)


