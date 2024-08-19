# def function1(arg1 , arg2):
#     print(10)

# def function1(*args):
#     if len(args) == 2:
#         print(10)
#     elif len(args) ==1:
#         print("Hello world")

# function1(1,2)

# class A:

#     def __init__(self, a):
#         self.a  =a
#     def __len__(self):
#         return len(self.a)

# class str:
#     def __len__(self):

# a = str("tr")
# print(len(a))
# print(len(A("10")))

# class Animal:
#     def speak(self):
#         return "method in Animal class"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "method in Dog class"
#
#
# print(Dog().speak())
# from math import pi
# class Shape:
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return pi*self.radius**2
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side**2
# class Triangle(Shape):
#     def __init__(self , base , height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         pass
#
#
# print(Triangle(5, 4).area())
"""
create
read
update
delete
"""

# users: list['User'] = []
# todos = []
#
#
# class CRUD:
#     def create(self):
#         pass
#
#     def read(self):
#         pass
#
#     def update(self, field , new_val):
#         pass
#
#     def delete(self):
#         pass
#
#
# class User(CRUD):
#     def __init__(self ,
#                  id : int= None,
#                  name: str= None ,
#                  age:int = None):
#         self.id = id
#         self.name = name
#         self.age = age
#
#     def create(self):
#         users.append(self)
#
#     def read(self):
#         for user in users:
#             if user.id == self.id:
#                 print(user.__dict__)
#
#     def update(self, field , new_val):
#         for user in users:
#             if user.id == self.id:
#                 if field == 'name':
#                     user.name = new_val
#                 elif field == 'age':
#                     user.age = new_val
#
#     def delete(self):
#         for i,user in enumerate(users):
#             if user.id == self.id:
#                 del users[i]
#
#     def sequence_id(self):
#         return users[-1].id + 1 if users else 1
#     def search(self, starts_name):
#         starts_name = starts_name.lower()
#         for user in users:
#             if user.name.lower().startswith(starts_name):
#                 print(user.__dict__)
#
#
# user1 = {
#     "id" : User().sequence_id(),
#     "name" : "Botir",
#     "age" : 25
# }
#
# user1 = User(**user1)
# user1.create()
# user2 = {
#     "id" : User().sequence_id(),
#     "name" : "Baxtiyor",
#     "age" : 25
# }
# user2 = User(**user2)
# user2.create()
# user2.search("B")


