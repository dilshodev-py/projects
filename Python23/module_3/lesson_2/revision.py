

# import random
# from string import ascii_uppercase as au

# 15:25
# a = "1 22 3 4 12 6 8 9"

# 1 - usul
# alfa = map(int , a.split())
# result = ""
# for i in alfa:
#     result += au[i-1] + " "
# print(result.rstrip())

# print(" ".join(map(lambda x : au[int(x) - 1] ,  a.split())))

# from itertools import compress

# def compress_(iterable , l : list[int]):
#     for i , v in enumerate(l):
#         if v:
#             yield iterable[i]


# print(list(compress_("ABCDEF", [1, 0, 1, 0,1])))
# print(list(compress("ABCDEF", [1, 0, 1, 0,1])))


# ===========================================

# def random_pass(num : int , length : int):
#     for _ in range(num):
#         # paswd = int(random.random()*10**length)
#         paswd = random.randrange(10**(6-1) , 10**length)
#         yield paswd
#
# print(list(random_pass(10, 6)))


# ========================================
# from collections import Counter
#
# world = ["helllo", "hi", "cars"]
# print(max(Counter("".join(world)).items(), key = lambda x : x[1])[0])

# world_str = "".join(world)
# d = {}
# for i in world_str:
#     d[i] = d.get(i, 0) + 1
#
# print(max(d.items(), key=lambda x: x[1])[0])

# def add(num1, num2):
#     return num1 + num2
#
# tmp = add
# print(tmp(1, 2))

# ======================================
# print("start")
# def plus_one(number): # 2
#     def add_one(number): # 4
#         return number + 1 # 5
#     result = add_one(number) # 3
#     return result # 6
# print(plus_one(4)) # 1

# ======================================

# def hello_function(): # 2
#     def say_hi(): # 5
#         return "Hi" # 6
#     return say_hi # 3
#
# hello = hello_function() # 1
# print(hello()) # 4

# =========================

# def uppercase_decorator(function):  # 2
#     def wrapper():  # 5
#         result = function()  # 6
#         make_uppercase = result.upper()  # 9
#         return make_uppercase  # 10
#
#     return wrapper  # 3
#
#
# def print_fullname():  # 7
#     return "botir jo'rayev"  # 8
#
#
# result = uppercase_decorator(print_fullname)  # 1
# print(result())  # 4

# ===========================================

# def uppercase_decorator(function):
#     def wrapper(*args):
#         result = function(*args)
#         make_uppercase = result.upper()
#         return make_uppercase
#
#     return wrapper
#
#
# @uppercase_decorator
# def print_address(region, district):
#     return f"{region} , {district}"
#
#
# print(print_address("tashkent", "sergili"))
#
#
# def two_pow(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         return result ** 2
#
#     return wrapper
#
#
# @pow(4)
# def add(num1, num2):
#     return num1 + num2
#
#
# print(add(2, num2=2))

# ===================================

# def poww(num):
#     def inner(function):
#         def wrapper(*args , **kwargs):
#             result = function(*args , **kwargs)
#             return result ** num
#         return wrapper
#     return inner

# @poww(3)
# def add(num1, num2):
#     return num1 + num2
#
# print(add(2, 2))

# =====================================================

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
#
#
# def is_auth(auth):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             for user in users:
#                 if user.get("username") == auth.get("username") and user.get("password") == auth.get("password"):
#                     return function(*args, **kwargs)
#             return "Bu funksiyadan foydalana olmaysan"
#
#         return wrapper
#
#     return inner
#
#
# session_user = {
#     "username": "jamol",
#     "password": "0000",
# }
#
#
# @is_auth(session_user)
# def summa(*args):
#     return sum(args)
#
#
# @is_auth(session_user)
# def add(num1, num2):
#     return num1 + num2
#
#
# print(add(1, 2))

# print(summa(1, 2, 3, 4, 5))


