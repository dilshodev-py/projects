"""Rivision"""
"""
unpacking
immutable -> str , int , float , bool , tuple , complex
hashable  -> str , int , float , bool , tuple , complex
a = (1,)
print(type(a))
type casting ->  a = 1
*args
**kwargs
* , /
"""
# def function(a , / , * ,b):
#     pass
# a, b, c = 1, 2, 3
# a = 1
# a = str(a)
# print(a)


# def calculator(*args):

# memory (stack , heap)
# id()
# while condition:
#     pass

# a = 10
# b = 20
# print(b) if b > a else print(a)

# maxi = lambda arg1 , arg2 : arg1 if arg1 < arg2 else arg2
# maxi(1, 9)

# a = "12fdsdg345         123     123             32456"
# a = "12fdsdg345 123 123 32456"
# summ = ""
# for i in a:
#     if i.isalpha():
#         summ += i
# print(summ)

# a = "12fdsdg345         123     123             32456"
# print(*a.split(), sep=' ')


# points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# l = []
# for i in points:
#     l.append(i[0])
# l.sort()
#
# maxi = l[1] - l[0]
# for i in range(1,len(l)-1):
#     maxi = max(l[i+1] - l[i] , maxi)
# print(maxi)

# words = ["abc","bcd","aaaa","cbc"]
# x = "a"
# l = []
# for i in range(len(words)):
#     if x in words[i]:
#         l.append(i)
# print(l)

# nums = [-1,1,2,3,1]
# target = 2
# c = 0
# for i in range(len(nums)):
#     for j in range(i+1 , len(nums)):
#         if nums[i] + nums[j] < target:
#             c += 1
# print(c)
#

# l = [(1, 2), (8, 7), (3, 5,1), (9, 5)]

# print(max(l , key=sum))
# print(max(l , key=lambda x : sum(x)))
# output : [8,7]

# l = [865,43,25678,53,723,41,7]
# print(sorted(l, key=lambda x : len(str(x))))
# print(min(l, key=lambda x: len(str(x))))
# print(max(l, key=lambda x: len(str(x))))
# sorted()


