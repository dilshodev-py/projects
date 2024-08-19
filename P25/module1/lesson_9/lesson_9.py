""""""
from sys import getsizeof

"""
mutable
immutable
hashable
unhashble 
memory : stack , heap
array - list , tuple , str 
algo : 0-129 , 145-172
codingbat
hakkerrank
leetcode -> 22 , 20 , 2 , 2 , 20 
"""

# mutable ->   list , set , dict , tuple
# immutable -> tuple , int , complex , str , float , bool

# l = [1,2,3,4]
# print(id(l))
# l.append(6)
# print(id(l))
#
# print("---------------")
# i = 10
# print(id(i))
# i += 2
# print(id(i))

# =========================================

# mutable
# immutable

# hashable  - immutable
# unhashble  - mutable

# l = [1,2,3]
# print(hash(l))

# i = "10"
# print(hash(i))


# tuple - immutable , mutable

# t = (1, 2, 3, 4, 5, [1, 2, 3])
# print(hash(t))


# list & tuple


# python.org
# t = (1,2,3,4,5)
# l = [1,2,3,4,5]
# for i in l:
#     print(i)

# from sys import getsizeof

# t = (1,2,3,4,5)
# l = [1,2,3,4,5]
# print(getsizeof(t))
# print(getsizeof(l))

# massiv - list , tuple , str
# collection - list , tuple , str
# array - list , tuple , str

# array -> [1,2,3,4,5,6]
# massiv -> [1,"1",3,4,5,6]

# l = [1, 2, 3, 234, 2345, 2345, 23456, 76, 45678, 9876, 234567, 9876, 4, 5]
# print(l[-1])
# print(l[-6])
# print(l[start:end :step])

# list out of range
# iterator
# for i in l:
#     print(i)
# sikl , index , slice , method


# tuple -> (1,2,3,4,5,6)

# for i in t:
#     print(i)
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o

# Usullar soni : 3 xil


# sikl , index , slice , method(2 ta)


# t = ("h", "e", "l", "l", "o")
# 1 - usul
# c = 0
# for i in t:
#     print(c, i)
#     c += 1

# 2 - usul
# for i in range(len(t)):
#     print(i, t[i])

# 3 - usul
# print(list(enumerate(t)))
# for i , v in enumerate(t):
#     print(i , v)

# i , v = (0, 'h') # unpacking
# print(v)

# s = "Hello Worldd"
# 1-usul
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         print(s[i])

# 2-usul
# for i , v in enumerate(s[:-1]):
#     if s[i] == s[i+1]:
#         print(v)

# 1/0
s = "I am go to School Today"

# 1 - usul
# t = ""
# for i in s:
#     if i.isupper():
#         t += i+" "
# print(t)

# 2 - usul
# print(" ".join([i for i in s if i.isupper()]))

# 3 - usul
# s = "I am go to School Today"
#
# for i in s:
#     if 65 <= ord(i) <= 90:
#         print(i , end = ' ')


# ============================================

# name = "7B7ot4ir Ka2mo123l Tohir"

# 1 - usul
# for i in name:
#     if i.isdigit():
#         print(i , end = "")
# 2 - usul
# for i in name:
#     if i in "012345789":
#         print(i , end = "")


# name = "7B7ot4ir Ka2mo123l Tohir"
# for i in name:
#     if i.isupper():
#         print(i.lower() , end = "")
#     elif i.islower():
#         print(i.upper() , end='')
#     else:
#         print(i , end = "")


# from string import punctuation
# name = "Hello Tohir"
#
# for i in name:
#     if i.isdigit() or i in punctuation:
#         print(False)
#         break
# else:
#     print(True)

# print(" ".join("Hello Tohir".split()[::-1]))

# s = "hello"
# "1 - module"
# summ = 0
# for i in range(len(s)-1):
#     summ += abs(ord(s[i]) - ord(s[i+1]))
# print(summ)

from string import ascii_lowercase

"""
dars:
    revision
    home work
    mavzu
    o'yin
    misollar
    Home Work
"""

"""
module 1 -> mavzu (algoritm) +
module 2 -> mavzu (project) +
module 3 -> advanced mavzu (project) 50/50
module 4 -> database mavzu (practic) +
module 5 -> advanced technology (project[tg bot]) 50/50

module 6
module 7
module 8         - Django + Fast Api  + Devops + Docker
module 9
module 10

staj
"""



