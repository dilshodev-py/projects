# import json
# from dataclasses import dataclass
# from os.path import join
# from pathlib import Path
#
# BASE_DIR = Path(__file__).parent
# DB_PATH = join(BASE_DIR, 'database')
#
#
# class DB:
#     @property
#     def objects(self):
#         file_name = self.__class__.__name__.lower() + "s.json"
#         with open(join(DB_PATH, file_name), 'r') as f:
#             data = json.load(f)
#         for i, d in enumerate(data):
#             data[i] = self.__class__(**d)
#         return data
#
#     def write(self, data: list):
#         file_name = self.__class__.__name__.lower() + "s.json"
#         for i, obj in enumerate(data):
#             data[i] = obj.__dict__
#         with open(join(DB_PATH, file_name), 'w') as f:
#             json.dump(data, f, indent=3)
#
#
# @dataclass
# class Product(DB):
#     id: int = None
#     name: str = None
#     price: float = None
#     quantity: int = None
#
#
# p = {
#     "id": 1,
#     "name": "Samsung S24",
#     "price": 1000,
#     "quantity": 2
# }
# products: list[Product] = Product().objects
# products.append(Product(**p))
# Product().write(products)
# import json

# l = {1, 2, 3, 4, 5, 6}
# d = l.copy()
# for i in d:
#     l.remove(i)


# with open('database/users.json' , 'r') as f:
#     d = json.load(f)
# res = []
# for i in d:
#     tmp = {}
#     for k , v in i.items():
#         if not isinstance(v , dict):
#             tmp[k] = v
#     res.append(tmp)
# with open('database/users.json', 'w') as f:
#     json.dump(res, f , indent=3)













