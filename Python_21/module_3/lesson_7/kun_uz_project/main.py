import httpx
from bs4 import BeautifulSoup

response = httpx.get("https://kun.uz/")
kun_html = response.text

soup = BeautifulSoup(kun_html , 'html.parser')
rows = soup.find_all('div' , {"class" : "col-md-6"})
for row in rows[:]:
    title = row.find('a' , {"class" : "small-news__title"})
    photo = row.find('a' , {"class" : "small-news__title"})
    if title:
        print(title.text)

    print()
    print()