""""""
from itertools import chain
from sys import getsizeof

"""
set    -  {} , set() 
    umumiy hususiyati  -> unique ,  shuffle , unhashble X, hashable  , mutable 

tuple  -  () , tuple()
    umumiy hususiyati  -> immutable , memory , fast , count , index , hashable , unhashable

"""
# print([1,2,3]*2)
# print((1, 2, 3) * 2)
# l = (1,2,3, [1,2,3])
# l[-1].append(4)
# print(l)


# t = tuple(range(1, 10))
# l = list(range(1, 10))
# print(getsizeof(t))
# print(getsizeof(l))
# =================== methods =================
# tuple
"""
count(obj) -> int
index(obj) -> int
"""
# set
"""
set().add(obj)
set().clear()
set().copy()
set().discard(obj)
set().remove(obj)
set().difference(iterable)
set().difference_update(iterable)
set().intersection(iterable)
set().intersection_update(iterable)
set().isdisjoint()
set().issubset(iterable)
set().issuperset(iterable)
set().pop()
set().symmetric_difference(iterable)
set().symmetric_difference_update(iterable)
set().union(iterable)
set().update(iterable)
"""
# a = {1,2,3}
# b = [4,5,6]
# print(a.update(b))
# print(a)
# print(a.union(b))

# nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# n = []
# for i in nums:
#     n.append(nums[i])
# print([nums[i] for i in nums])


# nums = [2,5,1,3,4,7]
# n = 3

# (l := []), [l.extend([nums[:n][i], nums[n:][i]]) for i in range(n)] , print(l)
# l = []
# for i in range(n):
#     l.extend([nums[:n][i] , nums[n:][i]])
# print(l)


# operations = ["--X", "X++", "X++"]
# print(-1 if "-" in i else 1 for i in operations)
#
# ball = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
# maxi = 0
# l = sorted([i[0] for i in ball])
#
# for i in range(1,len(l)):
#     maxi = max(maxi , l[i] - l[i - 1])
# print(maxi)

# map()
# [for i in iter]

# Telegram bot , Docker , Docker compose , SqlalchemyORM , database , redis , rabbitMq
# Telegram bot -> 300$ , 500$
# Essent Bot
# Fitnice Bot
# Post


# candies = [2, 3, 5, 1, 3]
# extraCandies = 3
# for i, item in enumerate(candies):
#     candies[i] = item + extraCandies >= m
# print(candies)
# (m := max(candies) ),print([item + extraCandies >= m for item in candies])

# support ->


# nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# tmp = []
# for i in nums:
#     c = 0
#     for j in nums:
#         if i > j:
#             c += 1
#     tmp.append(c)
# print(tmp)

# 2 version
# print([sum(i > j for j in nums) for i in nums])4





