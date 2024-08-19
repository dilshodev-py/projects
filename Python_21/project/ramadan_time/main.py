# import json
# from os.path import join
# from pathlib import Path
#
# BASE_DIR = Path(__file__).parent
# DB_PATH = join(BASE_DIR , 'database')
#
# with open(join(DB_PATH , "regions.json"), "r") as f:
#     data = json.load(f)
#
# result = {}
#
# for i in data:
#     id_ = i["viloyat"]["id"]
#     del i["viloyat"]["id"]
#     result[id_] = i["viloyat"]
#
# with open(join(DB_PATH , "regions.json") , "w") as f:
#     json.dump(result, f , indent=3)

# from datetime import date
#
# d = "2 Mart 2024".split()[::-1]
# d[1] = 3 if d[1] == "Mart" else 4
#
# data = date(*map(int , d))
# print(data == date.today())
from project.ramadan_time.ui.main import UI

UI().main()
