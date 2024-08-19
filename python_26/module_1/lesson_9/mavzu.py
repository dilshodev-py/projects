""""""

"""
tuple
set
matrix
"""

# list
# tuple

# t = "A", "B", "C" # packing
# print(type(t))

# print(t.index("A"))
# print(t.count("A"))
# index
# count
# clean code - pep8
# def test() -> tuple:
#     return 1, 2, 3, 4, 5

# print(test())
# ctrl + alt + L

# from sys import getsizeof
#
# l = [1, 3, 4]
# t = (1, 3, 4)
# print("list ", getsizeof(l))
# print("tuple ", getsizeof(t))

# import time
# start = time.time()
# for i in list(range(1,10**9)):
#     pass
# print(time.time()-start)
#
# start = time.time()
# for i in tuple(range(1,10**9)):
#     pass
# print(time.time()-start)
# b = (1,)
# print(type(b))
#
# b = 10_000_000
# print(b)
# s = [1,2,3, "a",4,5,6,877,9,1,1,1,1,1,1,1]
# s = set(s)

"""
add
clear
copy
discard
difference
difference_update
intersection
intersection_update
isdisjoint
issubset
issuperset
pop
remove
symmetric_difference
symmetric_difference_update
union
update
"""

# hashable    - int , str , float , complex , tuple , bool
# unhashable  - list , set , dict , tuple

# mutable     - unhashable
# immutable   - hashable

# print(hash("abs"))
# print(hash([1,2,3]))
# print(hash((1,2,3,4, (1, 2, 3))))

# l = (1,2,3,4,5 ,[1,2,3,4]) # unhashable
# l[5].append(10)
# print(l)

# l = [1, 2, 3, 4]
# print(id(l))
# l.append(10)
# print(id(l))
# print(l)

# =========================

# a = "10"
# print(id(a))
# a += "20"
# print(id(a))


# packing
# unpacking
#
# a = 1,2,3
# a , b , c = 1,2,3

# def test(*args, **kwargs):  # packing
#     pass
#
# test(*[1, 2, 3, 4, 5, 6])  # unpacking


# 3X3
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# matrix[0][0] , matrix[-1][-1] =  matrix[-1][-1],matrix[0][0]
# print(matrix)

matrix = [
    [100, 2, 3],
    [4, 5, 6 , 5 , 37 , 89],
    [7, 8, 9 , 10],
]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"({i},{j})" , end = " ")
    print()

"""
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2) (2,3)
"""

