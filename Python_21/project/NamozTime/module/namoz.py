from os.path import join
from pathlib import Path
from httpx import get
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).parent.parent
DB_PATH = join(BASE_DIR , 'database')


class Namoz:
    def __init__(self , link):
        self.link = link

    def time(self):
        html = get(self.link).text
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("div", {"class": "ad__item bor"})
        time = {}
        for row in rows:
            time[row.find("h2").text]  = row.find_all("p")[-1].text
        return time













