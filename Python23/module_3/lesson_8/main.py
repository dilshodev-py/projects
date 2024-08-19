# import csv
#
# import openpyxl
#
# with open('pandas/users.csv', mode='r') as f:
#     data = list(csv.DictReader(f))
#
#
# wb = openpyxl.Workbook()
#
# sheet = wb.active
#
# sheet.append(list(data[0].keys()))
# for i in data:
#     sheet.append(list(i.values()))
#
# wb.save('users.xlsx')
#
#
import json
from collections  import UserList , UserDict , UserString , namedtuple , OrderedDict , Counter

# name = UserString('Botir')
# print(name)

# l = UserList([1,2,3,4,5])
# d = UserDict({'k1' : 'v1' , 'k2' : 'v2'})
# print(d.data)

# d = OrderedDict({'k1' : 'v1' , 'k2' : 'v2'})
# d.move_to_end('k1')
# print(list(d.items()))


# for i in d.__dir__():
#     if not "__" in i:
#         print(i)

# class UserDTO:
#     def __init__(self , name , age , year):
#         self.name = name
#         self.age = age
#         self.year = year
#
# User = namedtuple('User' , ['name' , 'age' , 'year'])
#
# u1 = User('botir' , 25 , 1999)
# print(u1.year)
#
# a= Counter("1234565432123456")
# print(max(list(a.items()), key= lambda x : x[1])[0])

# Enum -> static(o'zgarmas datalar)
#
# from enum import Enum
#
# class PizzaSize(Enum):
#     small = 1
#     medium = 2
#     big = 3
#
#
# print(PizzaSize.small.value)
# print(PizzaSize(1).name)
# print(PizzaSize['big'].value)


# menu = """
#     Choose size
#     1) small
#     2) medium
#     3) big
#     >>>"""
# key = int(input(menu))
# print(PizzaSize(key).name)

# Dushanba
# Seshanba

# small
# medium
# big



# User = namedtuple('User' , ['id' , 'name'])
# u1 = User(1, 'botir')


with open('product.json' , 'r') as f:
    products:list[dict] = json.load(f)

for i,product in enumerate(products):
    p = namedtuple('Product' , list(product.keys()))
    products[i] = p(**product)

menu = products[0]._asdict().keys()

for pos , key in enumerate(menu,1):
    print(f"{pos}) {key}")
index = int(input(">>>")) - 1

for product in products:
    print(product[index])


# []     - list
# deque  -













