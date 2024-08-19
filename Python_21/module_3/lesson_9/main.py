import datetime
import time

import numpy as np # alies

# list , numpy 50X

# array = np.array(["Botir",2,3,4,5,6,7])
# array = np.array([[1,2,3], [4,5,6] , [7,8,9]])
# array = np.array([[[1,2,3], [4,5,6] , [7,8,9]]])
# array = np.array(42 , ndmin = 1)
# # array[1,2] = 10
# print(array)

# import numpy as np

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]] , ndmin = 3)
# print(arr)
# arr= arr.shape # 50X
#
# print(arr)


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,1,2,3,4,5,61,2,3,4])
#
# newarr = arr.reshape(-2)
#
# print(newarr)

from collections import UserList , UserString , UserDict , OrderedDict

# u = UserList()
# u.append("25")
# u.append("12")
# u.append("36")
# print(u[0])
# print(u[1])
# print(u[1:])
# u.sort(key = lambda x  :x[-1] , reverse = True)
# print(u)



# s = UserString("1Выбирать")
# print(s.lower())
# print(s.upper())
# print(s.upper())
# print(s.zfill(2))
# print(s.encode())


# d = UserDict({1:1 , 2:2})
# d["3"] = "Uch"
# d.update({"3" : "Uch"})
# print(d)

# o = OrderedDict()
# o.update({1:1})
# o.update({2:2})
# o.update({3:3})
# print(o.popitem(last=True))
# print(o.popitem(last=True))
# print(o.move_to_end(2))
# print(o)


""""""
from collections import Counter


# a = {1,2,3,4,5,1}
# a = {1:1 , 45:3}

# a = Counter(a)
# print(a.most_common(2))
# a.subtract([45])
# print(list(a.elements()))


# ENUM

# from enum import Enum
#
# class Season(Enum):
#     Spring = "1"
#     Summer = "2"
#     Autumn = "3"
#     Winter = "4"


# print(Season.Winter.value)
# print(Season("2").name)
# print(Season["Autumn"].name)
# print(Season["Autumn"].name)
# print(list(Season)[0].value)
#
# for i in Season:
#     print(i.name)

# menu = """
#     1) Spring
#     2) Summer
#     3) Autumn
#     4) Winter
#     >>>"""
# key = input(menu)
# print(Season(key).name)

import curses
import time

def main(stdscr):

    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        stdscr.addstr(0, 0, "Current Time: " + current_time)
        stdscr.refresh()
        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(main)


"""
collections
    list
    set
    tuple
    dict
    numpy        matrix
    UserString   string
    OrderDict    Dict
    UserList     list
    namedTuple   DTO
    Counter      Group By
    enum
    stack     
    queue
    Linked List
    
enum -> o'zgarmas (static) bo'lgan qiymatlal uchun
class PizzaSize(Enum):
    BIG = "Big"
    MEDIUM = "Medium"
    SMALL = "Small"

"""






