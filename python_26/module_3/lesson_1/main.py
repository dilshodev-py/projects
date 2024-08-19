# iterable - str , list , tuple , dict , set
# iterator -
# generator
import random
from itertools import count


# l = [1, 2, 3, 4, 5]
#
#
# while True:
#     try:
#         i = iter(l)
#         print(next(i))
#     except StopIteration:
#         break


def type_cast(x):
    return x % 2 == 1


# l = map(lambda x : str(x), [1, 2, 3])
# l1 = map(str, [1, 2, 3])
# l2 = map(type_cast, [1, 2, 3])
# print(list(l))
# print(list(l1))
# print(list(l2))

# f = filter(lambda x : x % 2 == 1, [1, 2, 3])
# f1 = filter(str, [1, 2, 3])
# f2 = filter(type_cast, [1, 2, 3])
# print(list(f))
# print(list(f1))
# print(list(f2))


# print(l)

# filter()

# for i in range(1, 10 ** 30):
#     print(i)

# def my_generator(count):
#     i = 1
#     while count >= i:
#         yield i
#         i += 1
#
#
# for i in my_generator(100):
#     print(i)


# def my_map(func , iterable):
#     for i in iterable:
#         yield func(i)

# def my_filter(func , iterable):
#     i = iter(iterable)
#     while True:
#         try:
#             res = next(i)
#             if func(res):
#                 yield res
#         except:
#             break
#
# for i in my_filter(lambda x : x > 10 , range(1,100)):
#     print(i)


# print(my_map(str , [2,3,4,5]))


from itertools import product


# def my_count(start=0, step=1):
#     while True:
#         yield start
#         start += step
#
#
# for i in my_count():
#     print(i)

# for i in product('ABCD', repeat=1):
#     print(i)

"""
tasks:
    0) cycle()
    1) range()
    2) count()
    3) repeat()
    4) accumulate()
    5) batched()
    6) chain()
    7) dropwhile()
    8) filterfalse()
    9) islice()
    10) takewhile()
    11) zip_longest()
    
    
link: https://docs.python.org/3/library/itertools.html
"""


# import random
#
# print(random.choice([1, 2, 3, 4, 5, 6]))

# names = [
#     "Botir",
#     "Komil",
#     "Mustaffo",
#     "Asilbek",
#     "Nodir",
#     "Komila",
#     "Jasur",
#     "Jamshid",
#     "Parvoz",
#     "Ikrom"
# ]

# [] ,  [i for i in names] , print()

# decorator

def decorator_name(num):
    def inner(func):

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            return res + num
        return wrapper
    return inner

@decorator_name(7)
def fib(n):
    return n + 20


print(fib(6))

