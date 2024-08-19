# def plus_one(number): # 1
#     def add_one(number): # 3
#         return number + 1 # 5
#     result = add_one(number) # 4 , 6
#     return result # 7
#
# print(plus_one(4)) # 2 , 8
import calendar
import time
from fractions import Fraction
from typing import Sequence

# def uppercase_decorator(function):
#     def wrapper(text_arg):
#         func = function(text_arg)
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
#
# @uppercase_decorator
# def hello(text):
#     return 'Hello ' + text
#
#
# print(hello("Dunyo"))


# def file_write(function):
#     def wrapper(*args, **kwargs):
#         result = str(function(*args, **kwargs))
#         with open('result.txt', 'a') as f:
#             f.write(f'{result}\n')
#         return result
#
#     return wrapper
#
#
# @file_write
# def print_data(data):
#     return data + "Make data"
#
#
# @file_write
# def add(num1, num2):
#     return num1 + num2


# =============================================


# def multiply(num):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             result = function(*args, **kwargs)
#             result = result * num
#             return result
#         return wrapper
#     return inner
#
# @multiply(10)
# @multiply(20)
# def add(a , b):
#     return a + b
#
# print(add(1, 2))


# def file(file_path, write=False):
#     def inner(function):
#         def wrapper(*args, **kwargs):
#             result = str(function(*args, **kwargs))
#             if write:
#                 with open(file_path, 'a') as f:
#                     f.write(result + '\n')
#             else:
#                 return result
#
#         return wrapper
#
#     return inner
#
#
# @file(write=False, file_path="/home/dilshod/PycharmProjects/python_26/module_3/lesson_2/test.txt")
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))


# =================================================================

# def function_time(function):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = function(*args, **kwargs)
#         end = time.time()
#         print("Function took {} seconds".format(end - start))
#         return result

#     return wrapper


# @function_time
# def add(a, b):
#     time.sleep(2)
#     return a + b


"""
home work
    @file(write=True)
    def calendar(y , m = None):
        pass
        
    
    read : 
        https://www.w3schools.com/python/ref_random_choices.asp
        https://www.geeksforgeeks.org/python-calendar-module/
        
    
    
"""

# ---------------------- random --------------------


# import random
#
# print(random.randrange(1, 20,step=2))
# print(random.randint(1, 20))
# print(str(int(random.random()*10**6)).ljust(6 , "0"))
# print(random.randbytes(10))
# print(random.choice(["olma", "banan", "nok"]))
# print(random.choices(["olma", "banan", "nok"],weights=[14,2,1], k=3))
# l = [1,2,3,4,5,6,7,8,9]
# random.shuffle(l)
# print(l)


# ----------------------- calendar --------------------------


import calendar

# yy = 2025
# mm = 12
# print(calendar.month(yy, mm))


# import calendar
# print ("The calendar of year 2018 is : ")
# print (calendar.calendar(2024))


# ------------------------ datetime , date -----------------------

# from datetime import datetime, date, tzinfo
#
# print(datetime.now())
# print(datetime.fromisoformat("2025-12-09").year)
# print(datetime.date(datetime.fromisoformat("2025-12-09")))
# print(datetime.replace(datetime.now() , year=2025))
# print(datetime.fromordinal(1000))
# print(datetime.today())
# print(datetime.timestamp(datetime.today()))
# a = datetime.timestamp(datetime.today())
# print(datetime.fromtimestamp(0))
# print(datetime.fromisocalendar(2024 , 2,1))
# print(datetime.strptime('2024-13-December', '%Y-%d-%B'))
#
# print(date.today())
# print(date.fromtimestamp(0))









