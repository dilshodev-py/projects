# pip install beautifulsoup4
#
# from bs4 import BeautifulSoup
#
# with open("index.html", "r") as f:
#
#     soup = BeautifulSoup(f.read(), 'html.parser')

# print(soup.find(id='link3'))
# print(soup.get_text())
#
# print(soup.find_all("p", {"class": "story"})[-1].text)
# print(soup.title)
# print(soup.p)
# print(soup.b)
# all_a = soup.find_all('a')
# for i in all_a:
#     print(i.text)
#     print(i["id"])
#     print(i["href"])

# print(soup.find("a", {"id": "link2"}))
# print(soup.find_all("a", {"id": "link2"}))

# ================================== really task =====================
# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get("https://www.orexca.com/uzbekistan/provinces.htm").text
# soup = BeautifulSoup(html, 'html.parser')
#
# section = soup.find("section", {"class": "col-md-8"})
# for i in section.find_all("li"):
#     print(i.text)

# ===================================================================

# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get("https://www.orexca.com/uzbekistan/provinces.htm").text
# soup = BeautifulSoup(html, 'html.parser')
#
# img = soup.find('img', {"alt" : "Map of Andijan Province. Click for resize"})
# img_url = "https://www.orexca.com" +img.get("src")
#
# img = requests.get(img_url).content
# with open("geog.png" , "wb") as f:
#     f.write(img)
# =================================================


# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get("https://www.orexca.com/uzbekistan/provinces.htm").text
# soup = BeautifulSoup(html, 'html.parser')
#
# img = soup.find('img', {"alt" : "Map of Bukhara Province. Click for resize"})
# img_url = "https://www.orexca.com" +img.get("src")
#
# img = requests.get(img_url).content
# with open("geog.png" , "wb") as f:
#     f.write(img)












