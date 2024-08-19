from datetime import date

from project.ramadan_time.model.ramadan import Ramadan


class UI:
    def main(self):
        regions = Ramadan().regions()
        Ramadan().region_show()
        key = input(">>>")
        region_link = regions[key].get('link')
        obj = Ramadan(region_name=region_link)
        is_bool = obj.is_infile()
        if is_bool:
            region_time: dict[dict] = obj.read()
        else:
            region_time : dict[dict] = obj.get_time()
        self.show_time(region_time)
        self.main()

    def show_time(self , region_time: dict[dict]):
        for date_ , value in region_time.items():
            d = date_.split()[::-1]
            d[1] = 3 if d[1] == "Mart" else 4
            data = date(*map(int , d))
            if data == date.today():
                text = f"Saharlik : {value.get('saharlik')}\nIftorlik : {value.get('iftorlik')}"
                print(text)



        