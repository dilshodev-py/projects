# a = "8"
# int()
# str()
# complex()
# list()
# set()
# tuple()
# dict()
# PEP8

# class User:
#     # def __init__(self , name : str = None , age : int = None) -> None:
#     #     self.name = name
#     #     self.age = age
#     def __init__(self , name , age) -> None:
#         self.name = name
#         self.age = age
#
#     def print_name(self):
#         print(self.name)
#
#     def print_year(self):
#         return 2023-self.age
#
#
#
#
# users = ["9"]
# while True:
#     name = input("Name : ")
#     age = int(input("Age : "))
#     u = User(name , age)
#     users.append(u)
#     key = input("continue [Yes/no] :")
#     if key == "no":
#         break
#
#
# l= ["a" , "u"]
#
# for i in users:
#     if isinstance(i , User):
#         print(f"Name : {i.name}, Age : {i.age}, Year : {i.print_year()}")



# a = str("hello")
# a.split()

# user1 = User("John", 23)
# for i in user1.__dir__():
#     if not "__" in i:
#         print(i)









# user1 = User()
# user2 = User("Botirjon" , 30)
# print(user1.age)
# print(user2.name)

# tuple([1,2,3]).count()

# class MyTuple:
#     def __init__(self, data):
#         self.data = data
#
#     def index(self, val , start=0 , stop=None):
#         if not stop:
#             stop = len(self.data)
#         for i,v in enumerate(self.data[start:stop]):
#             if v == val:
#                 return i+start
#
#     def count(self , val):
#         c = 0
#         for i in self.data:
#             if i == val:
#                 c += 1
#         return c



# my_massiv = MyTuple([1,2,3,4,5])
# print(type(my_massiv))
# print(my_massiv.count(4))

# with(open("text.txt" , "r")) as file:
#     numbers = file.read().split()
# result = []
# for i in numbers:
#     result.append(i[::-1])
# a = sorted(result)
# num = []
# for i in a:
#     z = i[1:]
#     num.append(z[::-1])
# print(num)


a = 7
b = 2
