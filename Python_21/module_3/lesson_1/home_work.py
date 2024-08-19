""""""
"""
iterable
    list , set , dict , tuple , str
    
iterator
    iter() , next()
    
generator
    def -> yield
    
itertools[generator] -> library

map(func , iterable)
filter(func , iterable)
"""

# list comprehension
# [item for item in iterable]
# dict comprehension
# l = dict([(1,1) , (2,2)])
# print(l)
# {1:1 , 2:2}
# {i : item for i , item in enumerate(iterable)}
# print({key: value for key, value in l})
# from itertools import product

# print(list(product("ABCD" , repeat = 2)))





# def product(iterable , repeat):
#     r = []
#     for i in iterable:
#         r.append((i,)*repeat)
#     print(r)

# def product(*args, repeat=1):
#     pools = [tuple(pool) for pool in args] * repeat
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         yield tuple(prod)
#
# print([1] + [2])
#
# for i in product("ABCD" , repeat=2):
#     print(i)




