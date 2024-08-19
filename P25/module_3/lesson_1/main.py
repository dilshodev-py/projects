""""""
"""
OOP :
    class 
    object
    abstraction
    encapsulation
    inheritance
    polymorphism
"""

# l = [1, 8, 3, 4] # iterable
# for iter in l: # iterator
#     print(iter)

# l = [1, 8, 3, 4]
# iterator = iter(l)
# while True:
#     try:
#         print(next(iterator))
#     except:
#         break

# for i in range(1, 100):
#     print(i)

# print(map(lambda x: x + 1, [1, 2, 3, 4]))
# for i in map(lambda x: x + 1, [1, 2, 3, 4]):
#     print(i)

# for i in map(lambda x: x + 1, [1, 2, 3, 4]):
#     print(i)

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield "Hello"
#
# for i in my_generator():
#     print(i)

# def my_range(*args):
#     start = 0
#     stop = 0
#     step = 1
#     if len(args) == 1:
#         stop = args[0]
#     elif len(args) == 2:
#         start, stop = args
#     elif len(args) == 3:
#         start, stop, step = args
#     while start < stop:
#         yield start
#         start += step


# range(10)
# for i in my_range(5, 10, 2):
#     print(i)

# def my_map(func, iterable):
#     for i in iterable:
#         yield func(i)

# for i in my_map(lambda x: x + 1, [1, 2, 3, 4, 5, 6]):
#     print(i)


# def my_filter(func, iterable):
#     for i in iterable:
#         if func(i):
#             yield i
#
#
# for i in my_filter(lambda x: x % 10 == 0, [2, 3, 4, 5, 6]):
#     print(i)

# def func1():
#     yield
#     yield
#     yield
#     yield
#     yield
#     yield

# STOP
# TIME: 16:30


# map
# filter
# range
#
# builtins func

from itertools import count, cycle, repeat, accumulate

# def my_count(start, step=1):
#     while True:
#         yield start
#         start += step
#
#
# for i in my_count(10,2):
#     print(i)

# def my_cycle(iterable):
#     while True:
#         for i in iterable:
#             yield i
#
#
# for i in my_cycle('absd'):
#     print(i)


# def my_repeat(value, count=-1):
#     while count != 0:
#         yield value
#         count -= 1
#
#
# for i in my_repeat(10,2):
#     print(i)


# def my_accumulate(iterable):
#     s = 0 if isinstance(iterable[0] , int) else ""
#     for i in iterable:
#         s += i
#         yield s

# def my_batched(iterable, n):
#     i = 0
#     while i < len(iterable)//n:
#         yield iterable[i*n:i*n+n]
#         i += 1
#     else:
#         yield iterable[i*n:]
#
# for i in my_batched([1,2,3,4,5], 3):
#     print(i)


# HOME WORK
"""
    compress()
    dropwhile()
    islice()
    takewhile()
    product()
"""


# d = {
#     "bir" : 1,
#     "ikki" : 2,
#     "uch" : 3,
#     "to'rt" : 4
# }

"""
ABCD
EFG
"""

# TIME: 17:27


import itertools
import collections

print(collections.Counter("11222"))
"""
iterable   - list , str , tuple , set 
iterator   - iter() , next()
generator  - def , yield
"""
