# class SanoqSistem10:
#     def __init__(self , num):
#         self.num = num
#
#     def chop_etish(self):
#         print(self.num)
#
# class SanoqSistema2(SanoqSistem10):
#     def chop_etish(self):
#         print(bin(self.num))
#
# class SanoqSistema8(SanoqSistem10):
#     def chop_etish(self):
#         print(oct(self.num))
#
# class SanoqSistema16(SanoqSistem10):
#     def chop_etish(self):
#         print(hex(self.num))
#
# SanoqSistema2(20).chop_etish()
#

# OOP tamoillari
#     class
#     object
#     inhertance
#     polymorphzm
#     encapsulation
#     abstraction

# ===================== iterable and iterator ===============
# a = [1, 2, 3, 4, 5, 7] # iterable

# for i in a:
#     print(i)
# iterator_a = iter(a) # iterator
# while True:
#     try:
#         print(next(iterator_a))
#     except StopIteration:
#         break

# iterator_a = iter(a) # iterator
# print(next(iterator_a)) # 1
# print(next(iterator_a)) # 2
# print(next(iterator_a)) # 3
# print(next(iterator_a)) # 4
# print(next(iterator_a)) # 5
# print(next(iterator_a)) # 7

# ====================== generator =========================

# print(list(range(1, 100)))
# print(list(map(str , [1,2,3])))
# range(10, 90)
#
# def my_range(*args):
#     start = 0
#     step = 1
#     if len(args) == 1:
#         end = args[0]
#     elif len(args) == 2:
#         start = args[0]
#         end = args[1]
#     elif len(args) == 3:
#         start = args[0]
#         end = args[1]
#         step = args[2]
#     while start < end:
#         yield start
#         start += step

# 16:20

# for i in my_range(100000000):
#     print(i)

# generator -> iterator
# iterator -X generator
# i = iter(my_range(1,7))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# def fibanach(amount):
#     s1 = 1
#     s2 = 1
#     if amount == 1:
#         yield s1
#     elif amount == 2:
#         yield s1
#         yield s2
#     else:
#         i = 2
#         yield s1
#         yield s2
#         while i < amount:
#             s3 = s1 + s2
#             yield s3
#             s1 = s2
#             s2 = s3
#             i += 1
#
# for i in fibanach(8):
#     print(i)


# 1
# 1
# 2
# 3
# 5
# 8

# def my_map(func , iterable):
#     # iterable = [(1,2) , (3,4)]
#     for i in iterable:
#         yield func(*i)

# def my_filter(func , iterable):
#     # iterable = [(1,2) , (3,4)]
#     for i in iterable:
#         if func(*i):
#             yield i

# print(my_map(str, [1, 2, 3, 4, 5]))
# print(list(my_map(str, [1, 2, 3, 4, 5])))
# print(list(my_map(lambda x : x*2, [1, 2, 3, 4, 5])))
# print(list(my_filter(lambda x,y : x == y , [(2,2) , (3,4)])))
# print(list(filter(lambda x,y : x == y , [(2,2) , (3,4)])))

# [2, 4]



# def function1(num):
#     return num * 10
# f1 = function1
# print(f1(10))


# ========================== itertools ========================

from itertools import count , cycle , dropwhile , chain

# for i in count(10):
#     print(i)

# def count(start , step = 1):
#     while True:
#         yield start
#         start += step

# for i in cycle([1,2,3]):
#     print(i)

# def cycle(iterable):
#     while True:
#         for i in iterable:
#             yield i
#
# for i in cycle([1,2]):
#     print(i)


# def repeat(value , rep = None):
#     if rep:
#         for i in range(rep):
#             yield value
#     else:
#         while True:
#             yield value
#
# for i in repeat(10):
#     print(i)




# def dropwhile(func , iterable):
#     iter_ = iter(iterable)
#     while True:
#         try:
#             tmp = next(iter_)
#         except:
#             break
#         if not func(tmp):
#             yield tmp
#             break
#     for i in iter_:
#         yield i

# print(list(dropwhile(lambda x : x < 5 , [1,6,2,4,1])))

# def takewhile(func, iterable):
#     shart = True
#     for i in iterable:
#         if shart and func(i):
#             yield i
#         else:
#             shart = False
#         if not shart:
#             break
# def takewhile(func, iterable):
#     for i in iterable:
#         if not func(i):
#             break
#         yield i
#
# for i in takewhile(lambda x: x < 5, [6, 2, 5, 1]):
#     print(i)


# 1
# ,
# 2
# ,
# 3
# 4
# 5
# 6
# 7
# 8


# def chain(*args):
#     for i in args:
#         yield from i
# for i in chain(["1,2,3"] , [4,5] , [6,7,8]):
#     print(i)

# def batched(iterable, n):
#     while True:
#         if len(iterable) <= n:
#             yield iterable
#             break
#         else:
#             yield iterable[:n]
#             iterable = iterable[n:]
# for i in batched([1, 2, 3, 4, 5, 6], 3):
#     print(i)










