import json
from os.path import join , exists
from pathlib import Path
from httpx import get
from bs4 import BeautifulSoup


BASE_DIR = Path(__file__).parent.parent
DB_PATH = join(BASE_DIR , 'database')

class File:
    def read(self):
        file_name = self.region_name + ".json"
        with open(join(DB_PATH , file_name) , 'r') as f:
            data:dict[dict] = json.load(f)
        return data

    def write(self, data : dict[dict]):
        file_name = self.region_name + ".json"
        with open(join(DB_PATH, file_name) , 'w') as f:
            json.dump(data , f, indent=3)




class WebRamadan(File):
    def __init__(self, region_name= None):
        self.region_name = region_name

    def get_time(self):
        link = f"https://namozvaqti.uz/ramazon/{self.region_name}"
        html = get(link).text
        soup = BeautifulSoup(html , 'html.parser')
        # return soup.find('table' , {"class" : "table table-sm table_calendar"})
        rows = soup.find_all('tr')[1:]
        result = {}
        for row in rows:
            info:list = row.find_all("td")

            result[info[2].text] = {
                    "day" : info[0].text,
                    "weekday": info[1].text,
                    "saharlik": info[3].text,
                    "iftorlik": info[4].text
                }
        self.write(result)
        return result



class Ramadan(WebRamadan):

    def is_infile(self):
        file_name = self.region_name + ".json"
        return exists(join(DB_PATH, file_name))

        # try:
        #     with open(join(DB_PATH , file_name), 'r') as f:
        #         json.load(f)
        #     return True
        # except:
        #     return False

    def region_show(self):
        with open(join(DB_PATH , "regions.json") , "r") as f:
            regions = json.load(f)
        regions = dict(sorted(list(regions.items()) , key = lambda x  :int(x[0])))
        for key , region in regions.items():
            print(f"{key}) {region.get('name')}")

    def regions(self):
        with open(join(DB_PATH , "regions.json") , "r") as f:
            regions = json.load(f)
        regions = dict(sorted(list(regions.items()) , key = lambda x  :int(x[0])))
        return regions




