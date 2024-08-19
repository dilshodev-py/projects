# from itertools import islice , product


# def my_islice(*args):
#     iterable = args[0]
#     start = 0
#     stop = None
#     if len(args) == 3:
#         start = args[1]
#         stop = args[2]
#     elif len(args) == 2:
#         stop = args[1]
#

#

# ======================= product ===============

from itertools import product


# def my_product(*iterables, repeat=1):
#     pools = [tuple(pool) for pool in iterables] * repeat

#     result = [[]]
#     for pool in pools:
#         result = [x + [y] for x in result for y in pool]

#     for prod in result:
#         yield tuple(prod)
#
# my_product('abcd', repeat=2)

# for i in my_product('ABCD', repeat=2):
#     print(i)


# ======================== revision ==========================

"""
iterator   - yes , iterable , generator
iterable   - list , tuple, set , str 
generator  - yes
yield      - yes
iter()     - iterator
next()     - iteratsiya
filter()   - yes
range()    - yes
map()      - yangi ro'yhat yasiydi
itertools  - generator orqali yasalgan funksiyalarni yozilgan kutibxonasi
collection - tezroq ishlidigan funksiyalar to'plami !
"""




