# """
# bcrypt
# abstraction
# work with text file
# """
# # alt + enter + enter
# # pip install bcrypt -> terminal
# # import bcrypt
# # salt = bcrypt.gensalt()
# # password = "1234".encode()
# #
# # hash_pass = bcrypt.hashpw(password, salt)
# # print(hash_pass)
# # after_pass = "1234".encode()
# # check_pass = bcrypt.checkpw(after_pass, hash_pass)
# #
# # print(check_pass)
#
# # passwords = []
# # while True:
# #     menu = """
# #         1) add
# #         2) check
# #         3) exit
# #         >>>"""
# #     match input(menu):
# #         case "1":
# #             salt = bcrypt.gensalt(12)
# #             password = input("Password : ").encode()
# #             hash_pass = bcrypt.hashpw(password, salt)
# #             passwords.append(hash_pass)
# #         case "2":
# #             password = input("Enter password : ")
# #             for hash_pw in passwords:
# #                 if bcrypt.checkpw(password.encode() , hash_pw):
# #                     print("Find password !")
# #                     break
# #             else:
# #                 print("Not found password")
#
#
# # FRONTEND     json    ->     hacker       ->    backend
#
# # shifr -> qaytarib bo'ladi (sha256 , md5 , sha1,ripemd-160)
# # hash  -> qaytarib bo'lmaydi
# # print(hash("1234"))
#
# # from abc import ABC, abstractmethod
# #
# #
# # class A(ABC):
# #     @abstractmethod
# #     def a(self):
# #         pass
# #
# #     @abstractmethod
# #     def b(self):
# #         pass
#
# # class B(A):
# #     def __init__(self,x , y):
# #         self.x = x
# #         self.y = y
# #
# #     def a(self):
# #         pass
# #
# #     def b(self):
# #         pass
# #
# #
# # print(B(1, 2))
#
#
#
# # Create
# # Read
# # Update
# # Delete
# #
# from abc import ABC, abstractmethod
#
#
# class CRUD(ABC):
#     @abstractmethod
#     def save(self):
#         pass
#
#     @abstractmethod
#     def get(self):
#         pass
#
#     @abstractmethod
#     def delete(self, id):
#         pass
#
#     @abstractmethod
#     def update(self, filed , new_val):
#         pass
#
#
#
#
# class User(CRUD):
#
#     def save(self):
#         pass
#
#     def get(self):
#         pass
#
#     def delete(self, id):
#         pass
#
#     def update(self, filed, new_val):
#         pass
#
#
# User().get()
#
# class Product(CRUD):
#
#     def save(self):
#         pass
#
#     def get(self):
#         pass
#
#     def delete(self, id):
#         pass
#
#     def update(self, filed, new_val):
#         pass
#
#
# class Order(CRUD):
#
#     def save(self):
#         pass
#
#     def get(self):
#         pass
#
#     def delete(self, id):
#         pass
#
#     def update(self, filed, new_val):
#         pass
#
#
# class Address(CRUD):
#
#     def save(self):
#         pass
#
#     def get(self):
#         pass
#
#     def delete(self, id):
#         pass
#
#     def update(self, filed, new_val):
#         pass
# import json
#
# with open("todos.json" , "r") as file:
#     todos = json.load(file)
#
# data = []
# for i in todos:
#     data.append("|".join(map(str, i.values())))
#
# print(*data, sep = "\n", file = open("todos.txt", 'a'))

# with open("todos.txt" , "r") as f:
#     todos_list = f.read().strip().split("\n")
# list_ = []
# for i in todos_list:
#     i = i.split('|')
#     print(i)
#     d = {
#         "userId" : int(i[0]),
#         "id" : int(i[1]),
#         "title" : i[2],
#         "completed" : True if i[3] == "True" else False
#     }
#     list_.append(d)
# print(list_)




