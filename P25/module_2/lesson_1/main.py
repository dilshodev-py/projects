# a = [1,2,3,4]
# print(id(a))
# a.append(5)
# print(id(a))


# b = "12345"
# print(id(b))
# b += "6"
# print(id(b))

# int()
# float()
# str()
# list()
# set()
# dict()
# tuple()
# bool()
# complex()
#
# a = "12345"

# Paskal Case


# ==================== object yaratish ================
#
# class User:
#     pass
#
# john = User()
#
#
# class Shape:
#     pass
#
# circle = Shape()
#
#
# class Animal:
#     pass
#
# obj = Animal()
#
# num = 10
#
#
# print("john" ,type(john))
# print("circle" ,type(circle))
# print("obj" ,type(obj))
# print("num" ,type(num))


# =================== class attribute yaratish ===========

# class User:
#     name = "John"
#     age = 30
#
#
# class Shape:
#     name = "Circle"
#     radius = 10
#
#
# class Animal:
#     name = "Monkey"
#     place = "Forest"


# user1 = User()
# user2 = User()
# user3 = User()

# print(user2.name , user2.age)
# user2.name = "Kamron"
# user2.age = 15
# print(user2.name , user2.age)

# print(user2.name , user2.age)
# user2.address = "Toshkent , sergili"
# print(user2.name , user2.age , user2.address)


# =============== class instance attribute =============

# class User:
#     def __init__(self, name , age):
#         self.first_name = name
#         self.age = age

# user1 = User("Yulduz" , 18)
# user2 = User("Suhrob" , 20)
# user2 = User("Suhrob" , 20)
# user2 = User("Suhrob" , 20)
# user2 = User("Suhrob" , 20)
# user2 = User("Suhrob" , 20)
# print(user1.first_name , user1.age , user1.address)
# print(user2.first_name , user2.age , user2.address)


# class Animal:
#     def __init__(self , name , place):
#         self.name = name
#         self.place = place
#
#
# animal1 = Animal("Wolf" , "Forest")
# animal2 = Animal("Monkey" , "Forest")
# print(animal1.name)
# print(animal1.place)
# print(animal2.name)
# print(animal2.place)


# junior -> staj 7+9 oy
# middle -> searching
# senior -> searching + staj
# bank -> 1200$ test

# my_str("Absdf")
# my_str.lower()

from string import ascii_uppercase, ascii_lowercase


# class MyStr:
#     def __init__(self, value):
#         self.value = value
#
#     def lower(self):
#         result = ""
#         lowercase = "abcdefghijklmnopqrstuvwxyz"
#         uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         for i in self.value:
#             if i in uppercase:
#                 index = uppercase.index(i)
#                 result += lowercase[index]
#             else:
#                 result += i
#         return result

# from string import ascii_lowercase,ascii_uppercase

# class MyStr:
#     def __init__(self,value):
#       self.value=value
#     def lower(self):
#         result=""
#         for i in self.value:
#             if i in ascii_uppercase:
#                 j=ascii_uppercase.index(i)
#                 result +=ascii_lowercase[j]
#             else:
#                 result+=i
#         return result
# v=MyStr("AbCd")
# print(v.lower())

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def mod(self):
        return self.num1 % self.num2

    def sub(self):
        return self.num1 - self.num2

    def pow(self):
        return self.num1 ** self.num2

    def div(self):
        return self.num1 / self.num2

    def multiple(self):
        return self.num1 * self.num2


#
# c = Calculator(2, 2)
# print(c.add())
# print(c.mod())
# print(c.multiple())
# print(c.div())
# print(c.pow())
# print(c.sub())
# c.mod()      # 0
# c.multiple() # 4
# c.div()      # 1
# c.pow()      # 4
# c.sub()      # 0


# ================================================

import datetime
class Staff:
    now_year = 2025

    def __init__(self,
                 first_name,
                 last_name,
                 age,
                 salary,
                 role,
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        self.role = role

    def year(self):
        result = self.now_year - self.age
        return result

    def info(self):
        result = f"""
ismi : {self.first_name}
familyasi : {self.last_name}
yoshi : {self.age}
oladigan oyligi : {self.salary}
lavozimi : {self.role}"""
        return result

    # def year(self):
    #     result = datetime.datetime.now().year - self.age
    #     return result


m = Staff("John", "Doe", 24, 2_000_000, "manager")
print(m.year())
print(m.info())

"""
ismi : John
familyasi : Doe
yoshi : 24
oladigan oyligi : 2000000
lavozimi : manager
"""

# a = 1_000
# print(a)
