import json

import httpx
from bs4 import BeautifulSoup
# pip install beautifulsoup4
text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Salom</title>
</head>
<body>
    <div>Hello World</div>
    <b class='1'>product1</b>
    <b class='2'>product2</b>
    <b class='3' id = 'product'>product3</b>
    <b class='4'>product4</b>
    <h1>product</h1>
</body>
</html>
"""

# soup = BeautifulSoup(text , 'html.parser')
# print(soup.find('b' , {'class' : "3"})['id'])


response = httpx.get('https://kun.uz/')
html = response.text

soup = BeautifulSoup(html , 'html.parser')
carts : list = soup.find_all('div', {"class": "col-md-6"})


data = []
for cart in carts:
    a = cart.find('a', {'class': "small-news__img"})
    if a:
        photo_link = a.find('img')['src']
        time = cart.find('div' , {'class':"news-meta"}).text
        title = cart.find('a' , {'class':"small-news__title"}).text
        d = {
            'photo_link' : photo_link,
            'time' : time,
            'title' : title
        }
        data.append(d)


for i, v in enumerate(data):
    image_byte = httpx.get(v.get('photo_link')).content
    with open(f"image/img{i}.png", 'wb') as f:
        f.write(image_byte)


with open('news.json', 'w') as f:
    json.dump(data , f , indent=3)





