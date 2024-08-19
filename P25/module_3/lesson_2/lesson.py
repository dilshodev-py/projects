# def function_name(a, b, c):
#     return a(b, c)
#
#
# def add(num1, num2):
#     return num1 + num2
#
#
# print(function_name(add, 10, 20))

# def plus_one(number): # 1
#     return number + 1 # 4
#
#
# add_one = plus_one # 2
# print(add_one(5)) # 3 , 5
#


# def plus_one(number):  # 1
#     def add_one(number):  # 2
#         return number + 1  # 4
#
#     result = add_one(number)  # 3 , 5
#     return result  # 6


# print(plus_one(4)) # 2 , 7


# ===========================================

# def plus_one(number):  # 1
#     return number + 1  # 6
#
#
# def function_call(function):  # 2
#     number_to_add = 5  # 4
#     return function(number_to_add)  # 5 , 7
#
#
# print(function_call(plus_one))  # 3 , 8

# ===========================================

# print(10)
# def hello_function():  # 1
#     def say_hi():  # 3
#         return "Hi"  # 7
#
#     return say_hi  # 4
#
#
# hello = hello_function()  # 2 , 5
# print(hello())  # 6 , 8

#
# def div_two(func):  # 1
#     def wrapper(*args, **kwargs):  # 4
#         result = func(*args, **kwargs)
#         return result / 2  # 8 , 10
#
#     return wrapper  # 5
#
#
# @div_two
# def add(num1, num2, num3, num4):  # 2
#     return num1 + num2 + num3 + num4  # 9
#
#
# @div_two
# def mul(a, b, c):
#     return a * b * c
#
#
# print(add(10, 20, 2, 30))


# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#
#     return wrapper
#
#
# @uppercase
# def say_hi(name):
#     return "hello there " + name
#
#
# print(say_hi("botir"))
#

# def clean_space(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         result = result.replace(' ', '')
#         return result
#     return wrapper
#
# @clean_space
# def print_text():
#     return "He        llo                Wor      ld!"
#
#
# print(print_text())
#


# def div(num):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result / num
#         return wrapper
#     return inner
#
#
# @div(5)
# def add(a, b):
#     return a + b
#
# print(add(10, 20))


# @slice_world(3)
# def make_world(text):
#     return text + "TEST"
#
#
# make_world("dssf df er dsfdrg efre4gt")  # ['dssf' ,'df', 'er']


import calendar

yy = 2024
mm = 6
print(calendar.month(yy, mm))