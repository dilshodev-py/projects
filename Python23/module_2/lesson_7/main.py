"""
print()
for , while
list comprehension
dict comprehension
lambda and def
unpacking
packing
immutable
mutable
hashable
unhashable
list , tuple
*args , **kwargs
OOP tamoillari
attribute and argument
konstruktor
open()
"""

"""rivision"""
"""
print()
"""


# print("Hello" , 1, sep='$' , file=open("print.txt" , 'a'))

# iterable -> list , str , set , tuple , dict


# for index , item in enumerate("12345"):
#     print(index , item)
#     if item == '3':
#         break
# else:
#     print("Finished For")
# data: list[tuple] = list(enumerate("12345"))
# print(data)

# data = "12345"
# i = 0
# while i < len(data):
#     print(data[i])
#     i += 1
# else:
#     print("Finished while")


# list comprehension
# l = [i for i in range(1,21) if i % 2 == 1]
# l = ['Juft' if i % 2 == 0 else "Toq" for i in range(1,21)]
# print(l)

# dict comprehension

# data = "students"
# d = {i**(2 if i % 2 == 1 else 1): v  for i , v in enumerate(data)}
# print(d)


# lambda and def

# def function_name():
#     # logic
#     print(10)

# def function_name():
#     print(10)
    # return None
    # return

# def function1(arg1 , arg2 , arg3):
#     print(1)
#
# def function2(*args):
#     print(type(args))
#
# def function3(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# def function4(*args , **kwargs):
#     print(kwargs)
#     print(args)
#
# function4(1,2,3 , name = "botir")

# def function5(a , b, c, / , d):
#     print(a , b , c , d)
#
# function5(1,2,c = 3 , d = "botir")

# def function6(a , b, c, * , d):
#     print(a , b , c , d)
#
# function6(1,2, 3 , d = "botir")


# lambda args : logic
# l = lambda num1 , num2 , num3 : (num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3)
# print(l(90, 90 , 90))

# l = lambda *args : sum(args)
# print(l(1,2,3,4))

# def logic row >= 3
# lambda logic row <= 3

# print((lambda *args: sum(args))(1, 2, 3, 4 , 5))

# unpacking ->
    # a , b , c , d = (1,2,3) , 2,3,4
    # is_bool , message = (True , "Success")

# def a(x , y):
#     print(x , y)
#
# l = [1,2]
# a(*l)  # unpacking

# def a(*args): # packing
#     print(args)
# #
# l = [1,2]
# a(1,2)  # unpacking
# a(*l)  # unpacking


# def a(**kwargs): # packing
#     print(kwargs)
# l = {"bir":1, "ikki": 2 , "uch" : 3}
# a(**l , is_file = True)  # unpacking
# a(bir = l.get("bir") , ikki = l.get("2"))  # unpacking

# packing
# a = 1,2,3,4,5,6,7


# class A:
#     def __init__(self , x , y):
#         self.x = x
#         self.y = y
#
#
# d = {"x" : 10 , "y" : 20}
# a = A(**d)


# immutable -> int , float , str , complex , bool , tuple
# mutable   -> list , dict , set , tuple

# hashable   -> immutable
# unhashable -> mutable

# import sys

# list , tuple
# l = [1,2,3]
# t = (1,2,3)
# print(sys.getsizeof(l))
# print(sys.getsizeof(t))


# OOP tamoillari
"""
    class         maket
    object        nusxa1
    inheritance   vorislik(single , multilevel , multiple , gbrid , herartichacal)
    encapsulation public , protected (_), private (__)
    polymorphism  overriding(python, PHP) , overloading(Java , C#....)
    abstraction   mavhumlik
"""


# attribute and argument

# class A:
#     def __init__(self , x,  y):
#         self.x1 = x
#         self.y1 = y

# file = open(file_path , mode = "[r , w , a , x]" )
# file.read()
# file.write()
# file.close()

# with open(file_path , mode = "[r , w , a , x]") as f:
#     f.read()

# with open("/home/dilshod/PycharmProjects/Python23/module_2/lesson_7/revision.py" , mode = "rb") as f:
#     print(f)
