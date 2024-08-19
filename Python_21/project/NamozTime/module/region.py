from bs4 import BeautifulSoup
from httpx import get



class Region:
    def __init__(self, link = None):
        self.link = link

    def district_list(self):

        html = get(self.link).text
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("div", {"class": "col-xl-4 col-xs-12 py-1"})
        districts = []
        for pos , row in enumerate(rows , 1):
            district = {
                "id" : pos,
                "link": row.find("a")["href"],
                "name": row.find("a").text,
            }
            districts.append(district)
        return districts

    def regison_list(self):
        html = get(self.link).text
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("div", {"class": "col-xl-4 col-xs-12 py-1"})
        regions = []

        for pos , row in enumerate(rows,1):
            region = {
                "id" : pos,
                "link": row.find("a")["href"],
                "name": row.find("a").text,
            }
            regions.append(region)
        return regions