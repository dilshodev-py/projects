# data type

"""
int
float
str
bool
complex
list
tuple
set
dict_
"""

# isinstance([False], list)
# print()
# abs()
# input()
# max()
# min()
# pow()
# type()
# str()
# int()
# float()
# list()
# set()
# dict_()
# tuple()
# bin()


# memory
from math import sqrt, cos, sin, log

"""
    stack     |   heap 
    variable  |   value
"""
# python ->  dynamic
# c++ , java , C# , PHP  -> static

# operators bitwise

"""
& -> and
| -> or
^ -> xor
>> -> kamayadi
<< -> oshadi
"""


# /  -> haqiqiy bo'lish
# // -> butunli bo'lish

# a = 1,2
# print(a)
"(1,2)"

# a , b = 1,2 # unpacking
# c = 1,2  # packing


# type casting (bitta type dan ikinchi type ga o'tish)
# int type - > str type


# index -> 0 1 2 3 ...
# space -> 1 2 3 4 ...


# ==================================================
# LOOP


# massiv = (1,2,"hi" , 4)
# for i in massiv:
#     print(i, end= " ")


# task1

# massiv = (1,2,3,4,5)
#
# s = 0
# for i in massiv:
#     s += i
# print(s)

# massiv = map(int , "1 2 3 4".split())
# s = 0
# for i in massiv:
#     s += i
#
# print(s)

# iterable = massiv

    # for ishlidigan xolat
    # str
    # list
    # tuple
    # set
    # dict_

    # for ishlamaslik xolat
    # int
    # float
    # complex
    # bool


# for i in {"name" : "Botirjon" , "age" : 25}.items():
#     print(i)
# g = 65432345
# g = str(g)
# s = 0
# for i in g:
#     s += int(i)
# print(s)


# a = input() # 1 2 3 4 3 2

# output:
    # 2
    # 4
    # 2


# str_num = input("NUM: ") # default type : STR 10305030
# result = ''
# for i in str_num:
#     if int(i) % 2 == 0:
#          i = '0'
#     result += i
# print(result)

"""
input:  '578349'
output: 9
"""
# number = input()
# maxi = 0
# for i in number:
#     if int(i) > maxi:
#         maxi = int(i)
# print(maxi)

# str_ = "hello"
# i = 0
# for item in str_:
#     print(i , item)
#     i += 1


# output
"""
0 h
1 e
2 l
3 l
4 o
"""


# n = int(input())
# S = 0
# hadi = 1
# while hadi <= n:
#     S += 1/hadi
#     hadi += 1
# print(S)
#
# for i in [1,2,3,4,5,6]:
#     if not i % 2:
#         break
#     print(i)


# https://algo.ubtuit.uz/problem/61


# from math import sin, factorial
# n = int(input())
# S = 0
# i = 1
# while i <= n:
#     S += sin(i)/pow(2,i)
#     i += 1
# print(f"{S:.2f}")


# https://algo.ubtuit.uz/problem/76

from math import pi
# a , b , c = map(int , input().split())
# S = 0
# x = a
# h = 3
# while x <= c:
#     S += pow((a*x + b)/(b**2+cos(x)**2), 1/3) - sin(x**2)/(a*b)
#     x += h

# print(f"{S:.2f}")


# https://algo.ubtuit.uz/problem/91
#
# from math import log , e
# a , b , c , d = map(int , input().split())
# S , P , SP = 0 , 1 , 0
# m, k , i = 1 , 1 , 1
#
#
# while m <= a:
#     S += (3 * m ** 3 + 4 * m + 5)/(m**3 + log(m, e))
#     m += 1
# m = 1
#
# while  k <= b:
#     P *= k / (k**3 + 7 * k + 5)
#     k += 1
#
# while  i <= c:
#     sp = 1
#     while m <= d:
#         sp *= (log(i , e) + pow(m , i))/(pow(m , i))
#         m += 1
#     SP += sp
#     i += 1
#     m = 1
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

































