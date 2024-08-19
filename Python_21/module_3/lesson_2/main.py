# def plus_one(number):
#     return number + 1
#
# add_one = plus_one
# print(add_one(5))
# print(plus_one(5))

# def plus_one(number): # 2
#     def add_one(number): # 4
#         return number + 1 # 5
#     result = add_one(number) # 3
#     return result # 6
#
#
# print(plus_one(4)) # 1

# def plus_one(number):
#     return number + 1
#
#
# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)
#
#
# print(function_call(plus_one))
# y = 20
# def a():
#     global y
#     y = 10
#     x
# print(y)

# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
# hello = hello_function()
# print(hello())

# def uppercase_decorator(function):
#     def wrapper(name):
#         name = name.upper()
#         func = function(name)
#         return func
#     return wrapper
#

# @uppercase_decorator
# def say_hi(name):
#     # name.upper()
#     return "hi there " + name
#
# print(say_hi("botiR"))
# hi there BOTIR


# def two_division(function):
#     def wrapper(*args):
#         func = function(*args)/2
#         return func
#     return wrapper
#
# @two_division
# @two_division
# @two_division
# def summa(*args):
#     return sum(args)
#
#
# print(summa(1, 2, 3, 4, 5))
# 17:03

# def division(num):
#     def inner(func):
#         def wrapper(*args):
#             return func(*args) / num
#
#         return wrapper
#
#     return inner


# @division(5)
# def summa(*args):
#     return sum(args)
#
# print(summa(1,2,3,4,5))


# def is_auth(function):
#     def wrapper(**kwargs):
#         for user in users:
#             if user.get("username") == kwargs.get("username") and user.get("password") == kwargs.get("password"):
#                 return function(**kwargs)
#         return "Not found account"
#     return wrapper

# @is_auth
# def account(**kwargs):
#     return f"Welcome {kwargs.get('username')}"
#
#
# print(account(username="baxa", password='1111'))
# # Not Found Account
# print(account(username="baxa", password='2222'))
# Welcome
# 17:25


# users = [
#     {
#         "id": 1,
#         "username": "botir",
#         "password": "1111",
#         "role": "ADMIN"
#     },
#     {
#         "id": 2,
#         "username": "baxa",
#         "password": "2222",
#         "role": "USER"
#     },
#     {
#         "id": 3,
#         "username": "jamol",
#         "password": "0000",
#         "role": "USER"
#     }
# ]
# def is_auth(function):
#     def wrapper(*args ,**kwargs):
#         for user in users:
#             if user.get("username") == kwargs.get("username") and user.get("password") == kwargs.get("password"):
#                 return function(*args, **kwargs)
#         return "Not found account"
#     return wrapper
# def permission(role):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             for user in users:
#                 if user.get('username')==kwargs.get('username') and user.get('password')==kwargs.get('password'):
#                     if role == user.get('role'):
#                         return function(*args)
#                     else:
#                         return 'Permission denied'
#         return wrapper
#     return inner


# @is_auth
# @permission(role = ["ADMIN" , "USER"])
# def summa(*args , **kwargs):
#     return sum(args)
#
# print(summa(1, 2, username="baxa123", password='2222'))
# # Not Found Account
# print(summa(1, 2, username="baxa", password='2222'))
# # 3
# print(summa(1, 2, username="botir", password='1111'))
# # permission denied


# def dec1(function):
#     def wrapper(*args):
#         print("dec1 start")
#         result = function(*args)
#         print("dec1 end")
#         return result
#     return wrapper
#
# def dec2(function):
#     def wrapper(*args):
#         print("dec2 start")
#         result = function(*args)
#         print("dec2 end")
#         return result
#     return wrapper
#
# @dec1
# @dec2
# def function(x,  y):
#     return x + y
#
#
# print(function(10, 20))

# import datetime
# date = "2023-01-01 12:12:12"
#
# date1 = datetime.datetime.fromisoformat(date)
#
# secund = date1.timestamp()
# print(datetime.datetime.fromtimestamp(1672557132.0))
#


