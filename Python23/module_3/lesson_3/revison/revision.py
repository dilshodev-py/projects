"""decorator"""
# from datetime import datetime
import time

"""
            decorator
            
def decorator_name(arg1, arg2):
    def inner(function)
        def wrapper(*args , **kwargs):
            logic
        return wrapper
    return inner
    
    
"""


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
# ]  # database
#
#
# def permission(role: list[str]):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             if kwargs.get("user").get("role") in role:
#                 return function(*args)
#             else:
#                 return "Permission denied !"
#         return wrapper
#
#     return inner
#
# def is_auth(function):
#     def wrapper(*args, **kwargs):
#         for user in users:
#             if user.get("username") == kwargs.get("username") and user.get("password") == kwargs.get("password"):
#                 kwargs.update({"user" : user})
#                 return function(*args , **kwargs)
#         return "Not found account"
#     return wrapper
#
#
# @is_auth
# @permission(role=["ADMIN"])
# def summa(num1, num2):
#     return num1 + num2


# @is_auth
# @permission(role=["ADMIN"])
# def save(user: dict):
#     users.append(user)

# print(summa(1, 2, username="baxa", password='2222'))
# print(summa(1, 2, username="baxa", password='2222'))
# print(summa(1, 2, username="botir", password='1111'))
# user = {
#         "id": 5,
#         "username": "Polat",
#         "password": "0001",
#         "role": "USER"
# }
# print(save(user, username='baxa', password="2222"))
# print(users)


# file = False bo'lsa print qilinsin
# file = True bo'lsa file ga yozilsin


# import calendar
# def to_print(file):
#     def inner(function):
#         def wrapper(*args , **kwargs):
#             result = function(*args, **kwargs)
#             if file:
#                 with open("calendar.txt" , "w") as f:
#                     f.write(result)
#             else:
#                 return result
#
#         return wrapper
#     return inner
#
# @to_print(file = False)
# def create_calendar(*args):
#     if len(args) == 1:
#         return calendar.calendar(*args)
#     elif len(args) == 2:
#         return calendar.month(*args)
#     else:
#         print("Bad argument")
#
#
# print(create_calendar(2025,4,5))


# def datetime_valid(function):
#     def wrapper(*args , **kwargs):
#         try:
#             datetime.fromisoformat(*args , **kwargs)
#             return function(*args, **kwargs)
#         except:
#             return "Invalid datetime"
#
#     return wrapper
#
#
#
#
# @datetime_valid
# def print_datetime(date_time : str):
#     print(date_time)
#
#
# print(print_datetime("2024-03-18 23:59:00"))


# def log_function_call(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         with open("log.txt", 'a') as f:
#             f.write(str(result) + "\n")
#         return result
#
#     return wrapper
#
#
# def time_(function):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = function(*args, **kwargs)
#         print("Time :", time.time() - start)
#         return result
#
#     return wrapper


# @time_
# @log_function_call
# def add(num1, num2):
#     time.sleep(2)
#     return num1 + num2
#
#
# print(add(1, 2))
