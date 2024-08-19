# import asyncio
# import httpx
# from bs4 import BeautifulSoup
#
#
# class Weather:
#     def __init__(self, link):
#         self.link = link
#     async def weather(self):
#         async with httpx.AsyncClient() as client:
#             data = await client.get(self.link)
#         html = data.content
#         soup = BeautifulSoup(html, 'html.parser')
#         select = soup.find('table' , {"class" : "weather-table"})
#         selections = select.find_all('tr')
#         return selections
#     async def regions(self): # NOQA
#         async with httpx.AsyncClient() as client:
#             data = await client.get(self.link)
#             html = data.content
#         soup = BeautifulSoup(html, 'html.parser')
#         html = soup.find('ul' , {'class' : 'list-c'})
#         regions = []
#         for i in html.find_all('a'):
#             regions.append({"link" : i.get('href'), "region_name" : i.text})
#         return regions
#
# class UI:
#     async def main(self):
#         obj = Weather("https://obhavo.uz/")
#         regions = await obj.regions()
#         for pos , region in enumerate(regions,1):
#             print(f"{pos}) {region.get('region_name')}")
#         key = int(input(">>>"))
#         link = regions[key-1].get('link')
#         obj = Weather(link)
#         selections = await obj.weather()
#         for i in selections:
#             print(*i.get_text().strip().split('\n'))
#             print()
#
# asyncio.run(UI().main())
