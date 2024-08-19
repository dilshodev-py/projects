"""
5-module
telegram bot
sqlalchemy
payment
Web Admin
Docker
RabbitMq
Redis
"""

"""
iterable
iterator
generator
"""

# massiv = [1, 2, 3, 4, 5, 6, 7]


# class MyClass:
#     def __init__(self, massiv):
#         self.massiv = massiv
#         self.pos = 0

#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         x = self.massiv[self.pos]
#         self.pos += 1
#         return x


# m = iter(massiv)
# while True:
#     try:
#         print(next(m))
#     except StopIteration as message:
#         print(message)
#         break

# for i in massiv:
#     print(i)

"""
for (int i = 1 , i < 100 , i++) {
    
}
"""

"""

iterable
    list
    tuple
    set
    dict
    str
    
iterator
    list
    tuple
    set
    dict
    str
    generator
"""

# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

# m = map(int , ["1" , "2" , "3" , "4"])
# print(list(m))

# def generator(num):
#     start = 1
#     while num > start:
#         yield start
#         start += 1
# a = generator(100000000000000)
# import itertools
# def my_range(*args):
#     start = 0
#     step = 1
#     if len(args) == 1:
#         end = args[0]
#     elif len(args) == 2:
#         start = args[0]
#         end = args[1]
#     elif len(args) == 3:
#
#         start = args[0]
#         end = args[1]
#         step = args[2]
#     else:
#         raise Exception("error")
#     if args[2] > 0:
#         while start < end:
#             yield start
#             start += step
#     elif args[2] < 0:
#         start, end = end, start
#         while start < end:
#             yield end
#             end += step


# m = list(my_range(10, 20, -2))
# m = list(range(100, 10, -2))
# print(m)

# range(10,100)

# 17:00

# from datetime import datetime
# from pydantic import BaseModel


# class User(BaseModel):
#     id: int
#     name: str
#     signup_ts: datetime | None
#     friends: list[int]


#
# external_data = {
#     "id" : "1",
#     "name" : "Botir",
#     "signup_ts" : datetime.now(),
#     "friends": ["1" , "1"]
#
#
#
# }
# user = User(**external_data)

# def filter_(func , iterable):
#     for i in iterable:
#         if func(i):
#             yield i

# def map_(func , iterable):
#     for item in iterable:
#         yield func(item)


# l = list(filter(lambda num : num % 2 == 1 , [1,2,3,4,5]))
# l = list(map_(lambda num : 0 if num % 2 == 0 else num, [1,2,3,4,5]))


# def count(start , step = 1):
#     while True:
#         yield start
#         start += step
#
#
# def cycle(item):
#     while True:
#         for i in item:
#             yield i

# import itertools

# i = list(itertools.accumulate("12345"))
# print(i)

# def accumulate_(*args):
#     for i, elem in enumerate(args):
#         j = 0
#         if isinstance(elem, str):
#             res = ""
#         elif isinstance(elem, list):
#             res = []
#         else:
#             res = 0
#         while j <= i:
#             res += args[j]
#             j += 1
#         yield res
#
# a = accumulate_([[1,2] , [1,2]])
# print(list(a))


# print(list(itertools.accumulate([[1, 2, 3], [1, 2, 3]])))
# for i in accumulate_([[1,2],[1,2]]):
#     print(i)
# print(list(itertools.repeat(10)))
# def repeat(a, b:int=None):
#     # if b == 0:
#     #     while True:
#     #         yield a
#     # else:
#     #     for i in range(b):
#     #         yield a
#     i = b
#     while True if not i else b:
#         yield a
#         if b:
#             b -= 1


# 10
# 11
# 12
# 13
# ...

