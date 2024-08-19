# import numpy
# game = [
#     ["#" , "." , "#"],
#     ["." , "#" , "."],
#     ["#" , "." , "."],
#     ["#" , "." , "#"],
#     ["#" , "." , "."]
# ]
# game = numpy.array(game)
# for i in range(len(game)):
#     for j in range(len(game[0])):
#         if game[i,j] == "#":
#             game[i,j] = '.'
#             k = -1
#             while game[k,j] != '.':
#                 k -= 1
#             game[k,j] = '#'
# print(*game, sep='\n')


# [
#     ["." , "." , "."],
#     ["." , "." , "."],
#     ["." , "." , "."],
#     ["#" , "." , "#"],
#     ["#" , "#" , "#"]
# ]


# l = [1,2,3,4]
# l[2:] = [10]
# print(l)
from collections import namedtuple
from enum import Enum

# class Color(Enum):
#     GREEN = 1
#     YELLOW = 2
#     WHITE = 3
#     BLACK = 4

# print(Color.YELLOW.value)
# print(Color.YELLOW.name)
# print(Color(2).name)
# print(Color["YELLOW"].value)
# for i in Color:
#     print(i.value)

# class StudyEnum(Enum):
#     School = 1
#     Litsey = 2
#     Unversity = 3

# menu = """
#     Where are you study ?
#     1) School
#     2) Litsey
#     3) Unversity
#     >>>"""
# key = int(input(menu))
# print(StudyEnum(key).name)


# choose gender
#
# Male      Female

# MALE
# FEMALE

# class GenderEnum(Enum):
#     MALE = "Male"
#     FEMALE = "Female"

from datetime import date
# class Weekday(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7
#
# day = input("Week name : >>>")
# print(Weekday[day].value)
# print(Weekday(5).value)


#
# users = namedtuple("Users" , ['user_id' , 'firstname' , 'last_name' , 'address' , 'email'])
# products = namedtuple("Products" , ['product_id' , 'name', 'description' ,'price' ])
# orders = namedtuple("Orders" , ['order_id' , 'user_id' , 'product_ordered' , 'total_paid'])
#
#
# u1 = users(1 , 'botirjon' , 'botirov' , 'Tashkent' , 'botir@gmail.com')
# print(u1.firstname)
