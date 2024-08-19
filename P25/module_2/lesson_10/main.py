"""doc"""

from abc import abstractmethod
from dataclasses import dataclass

"""class decorator"""

# @dataclass
# class Phone:
#     id: int = None
#     name: str = None
#     model: str = None
#     colors: list = None
#     price: int = None
#     storage: int = None
#
#     @property
#     def info_print(self) -> None:
#         print("id : " , self.id)
#         print("name : " , self.name)
#         print("model : " , self.model)
#         print("colors : " , self.colors)
#         print("price : " , self.price)
#         print("storage : " , self.storage)
#         return
#
#     @classmethod
#     def from_str(cls , data : str ):
#         return cls(*data.split(','))
#
#     @staticmethod
#     def calculator(num1, operator: int, num2):
#         return eval(f"{num1} {operator} {num2}")
#
# print(Phone())


# Phone(model="24 ultra" , colors=['black' , 'white' , 'gold'] ,name='Samsung' , id=1 , storage=256 , price=1000 ).info_print

# print(Phone.from_str("1,Samsung,24 ultra,'black'|'white'|'gold',1000,256"))


# print(Phone.calculator(10, "*", num2=20))


"""try/Except/raise"""

# a = 10
# if a != 0:
#     print(a)

# marks = 10000
# a = marks / 0
# print(a)

# x = 5
# y = "hello"
# z = x + y
# print(10)

# result = int(float('1.10'))
# print(result)


# marks = 10000
# try:
#     result = marks / 1
# except:
#     print("Xatolik yuz berdi !")
# else:
#     print("Code mofaqiyatli bajarildi")
# finally:
#     print("Code fazifasini tugatdi!")
#
# print("Hello world !")

"""
"Code mofaqiyatli bajarildi"
"Code fazifasini tugatdi!"
"Hello world !"
"""

# class MyException(Exception):
#     pass


# try :
#     raise MyException("My Exception tomonidan xatolik chiqdi")
# except (MyException , ValueError) as m:
#     print(m)
