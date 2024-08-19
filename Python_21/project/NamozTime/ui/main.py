from enum import Enum

from project.NamozTime.lang.main import data
from project.NamozTime.module.namoz import Namoz
from project.NamozTime.module.region import Region

session_lang = "UZ"


class LanguageEnum(Enum):
    EN = 1
    UZ = 2
    RU = 3
class UI:
    def region(self):
        lang_data = data.get(session_lang)
        regions : list[dict] = Region(f"https://namozvaqti.uz/{session_lang.lower()}/viloyat").regison_list()
        for region in regions:
            print(" "*5,f"{region.get('id')}) {region.get('name')}")
        key = input(f"{lang_data.get('choose')} : ")
        link = regions[int(key) - 1].get("link")
        self.district(link)

    def district(self, link):
        lang_data = data.get(session_lang)
        districts: list[dict] = Region(link).district_list()
        for district in districts:
            print(" "*5 , f"{district.get('id')}) {district.get('name')}")
        key = input(f"{lang_data.get('choose')} : ")
        link = districts[int(key) - 1].get("link")
        self.show_time(link)
    def show_time(self, link):
        time: dict = Namoz(link).time()
        for name , time in time.items():
            print(" "*10 , f"{name} : {time}")
        self.main()


    def main(self):
        lang_data = data.get(session_lang)
        menu = f"""
    1) {lang_data.get("prayer")}
    2) {lang_data.get("suras")}
    3) {lang_data.get("lang")}
    4) {lang_data.get("exit")}
    >>>"""
        key = input(menu)
        match key :
            case "1":
                self.region()
            case "2":
                pass
            case "3":
                self.change_lang()
            case "4":
                return

    def change_lang(self):
        global session_lang
        for i in LanguageEnum:
            print(f"{i.value}) {i.name}")
        print("0) back")
        key = int(input(">>>"))
        session_lang = LanguageEnum(key).name

        self.main()




