# decorators function

# def add(x , y):
#     return x + y
# print(id(add))
# p = add
# print(p(1, 2))
# print(add(1, 2))
"""
stack   |    heap
add        139926971415952
p
"""

# def function1():
#     print("function 1")
#     return "Hello world"
#
# def function2():
#     print("function2")
#     return function1()
#
# print(function2())

# def function1():
#     return "Hello world"

# def function2():
#     return function1
# #
# print(function2()())

"global , local"
# def function2(other_function):
#     def function1():
#         return other_function
#     return function1
# def add(x,  y):
#     return x + y
# print(function2(add)()(1, 2))


# a = 10
# def function():
#     global a
#     a = 20
# function()
# print(a)


# def decorator(func):
#     print("start decorator")
#     def wrapper(*args):
#         print("start wrapper")
#         return func(*args) + 10
#     return wrapper

# @decorator
# def mul(x , y):
#     print("start mul")
#     return x * y
# print(mul(1,  10))


# def lower(func):
#     print("start lower")
#     def wrapper(*args):
#         print("start wrapper")
#         if len(args) == 1:
#             result = func(*args)
#             print("end wrapper")
#             print("end lower")
#             return result.lower()
#         return "Kiritilgan argumentlar ko'p"
#
#     return wrapper
#
#
# def is_admin(func):
#     def wrapper(user: dict):
#         if user['role'] == "ADMIN":
#             return func(user)
#         return "Sizda huquq yo'q"
#     return wrapper
#
#
#
# @is_admin
# def add_book(user):
#     print(user)
#
# @my_property
# def delete_book(user):
#     print(user)
#
# user = {
#     "fullname" : "Botirjon",
#     "role" : "USER"
# }
#
# print(add_book)


# print(decorator(mul)(2, 6))

# def my_property(func):
#     def wrapper():
#         return func()
#     return wrapper()
#
# @my_property
# def print_hello():
#     print("Hello world")
#
#
# print_hello


def mul(num = 1):
    print("start" ,num)
    def inner(func):
        def wrapper(*args):
            result = func(*args)
            print("end" , num)
            return result*num
        return wrapper
    return inner


def div(num):
    print("start", num)

    def inner(func):
        def wrapper(*args):
            result = func(*args)
            print("end", num)
            return int(result / num)

        return wrapper

    return inner

@hash_password
def create_account(user: dict):
    pass


# @div(4)
# @div(3)
# @mul(2)
# @mul(3)
# def add(*args):
#     print("main function")
#     return sum(args)
# print(add(5,5))





