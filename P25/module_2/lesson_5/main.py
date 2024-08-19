# polymorphism


# def add(num1, num2):
#     return num1 + num2
#
#
# def add(num1, num2, num3):
#     return num1 + num2 + num3
#
# print(add(1, 2))

# Python - dynamic
# Java , C++ - static

#
# class Employee:
#     def calculate_salary(self):
#         pass
#
# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         return 50000
#
# class PartTimeEmployee(FullTimeEmployee):
#
#     def calculate_salary(self):
#         return 20000
#
#
# fte = PartTimeEmployee()
# print(fte.calculate_salary())


# =================================================

# class Staff:
#     def __init__(self , name):
#         self.name = name
#
#     def role(self):
#         pass
#
#
# class Manager(Staff):
#
#     def role(self):
#         return "Manager"
#
#
# class Developer(Staff):
#     def role(self):
#         return "Developer"
#
#
# class SalesPerson(Staff):
#     def role(self):
#         return "Sales"
#
# m = SalesPerson('Botir')
# print(m.role())


# =============================================
# import math
#
#
# class Shape:
#
#     def area(self):
#         pass
#
#
# class Circle(Shape):
#     pi = math.pi
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return self.pi * (self.radius ** 2)
#
#
# class Square(Shape):
#
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return (self.base * self.height) / 2


# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def calculate_salary(self):
#         pass
#
#
# class HourlyEmployee(Employee):
#     def __init__(self, name, hours_worked, hourly_rate):
#         super().__init__(name)
#         self.hours_worked = hours_worked
#         self.hourly_rate = hourly_rate
#
#     def calculate_salary(self):
#         return self.hours_worked * self.hourly_rate
#
#
# class SalariedEmployee(Employee):
#     def __init__(self, name, annual_salary):
#         super().__init__(name)
#         self.annual_salary = annual_salary
#
#     def calculate_salary(self):
#         return self.annual_salary / 12
#
#
# class CommissionEmployee(Employee):
#     def __init__(self, name, sales_amount, commission_rate):
#         self.sales_amount = sales_amount
#         self.commission_rate = commission_rate
#         super().__init__(name)
#
#     def calculate_salary(self):
#         return self.sales_amount * self.commission_rate

# users: list['User'] = []
# products: list['Product'] = []
#
#
# class CRUD:
#     def create(self):
#         pass
#
#     def update(self, attribute, new_value):
#         pass
#
#     def delete(self):
#         pass
#
#     def read(self):
#         pass
#
#
# class User(CRUD):
#     def __init__(self,
#                  id: int,
#                  fullname: str,
#                  age: int,
#                  address: str):
#         self.id = id
#         self.fullname = fullname
#         self.age = age
#         self.address = address
#
#     def create(self):
#         users.append(self)
#
#     def update(self, attribute, new_value):
#         for user in users:
#             if user.id == self.id:
#                 if attribute == 'fullname':
#                     user.fullname = new_value
#                 elif attribute == 'age':
#                     user.age = new_value
#                 elif attribute == 'address':
#                     user.address = new_value
#
#     def delete(self):
#         for user in users:
#             if user.id == self.id:
#                 users.remove(user)
#
#     def read(self):
#         return users
#
#
# class Product(CRUD):
#     def __init__(self,
#                  id: int,
#                  name: str,
#                  price: float,
#                  quantity: int):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def create(self):
#         products.append(self)
#
#     def update(self, attribute, new_value):
#         for product in products:
#             if product.id == self.id:
#                 if attribute == 'name':
#                     product.name = new_value
#                 elif attribute == 'price':
#                     product.price = new_value
#                 elif attribute == 'quantity':
#                     product.quantity = new_value
#
#     def delete(self):
#         for product in products:
#             if product.id == self.id:
#                 products.remove(product)
#
#     def read(self):
#         return products




# 1.Introduction
# ~ Kirish - kurs nima haqida, mentor haqida umumiy ma'lumot
# ~ Umumiy kurs haqida, kursdan nimalar oladi.
#
# 2. Setup
# ~ IntelliJ IDEA - download, setup, run
# ~ Create a new Java project in IntelliJ IDEA
# ~ TelegramBot kutubxonalarini import qilish
# ~ Bot qanday yaratiladi
#
# 3. Bot Programming
# ~ Bot Tokenlarini o'rnatish
# ~ Update Object
# ~ Reply to Messages
# ~ Chat commandlarini yaratish
# ~ filters
# ~ Tg telefon nomerini olish
# ~ Emojilar jo'natish
# ~ Yuzaga kelishi mumkin bo'lgan muammolarni sanab o'tish va ularga yechimlar berish
#
# 4. json file bilan ishlash
# ~ file ga kirish usulari
# ~ json file yaratish
# ~ json file ga yozish
# ~ user data save to json
# ~ Saqlangan userlarni topish va yangi user kiritish
# ~ Saqlangan user malumotlaridan foydalanish
#
# 5. Auto Reply message Bot

# 6. Deploy to Server


