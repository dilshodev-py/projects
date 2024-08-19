""""""
import collections
from collections import Counter
from itertools import chain, takewhile, combinations
from typing import List

"""
print(sep= , end=)
int('1010', 8)
float('-inf')
float('inf')
hashable 
unhashable 
immutable 
mutable
string [split , slice , replace , find , count]
list   [pop , find , join , append, remove , extend , sort , reverse, clear]
set    [unique, add , remove , count]
dict   [values , keys , get , pop , popitem , fromkeys , items]
function [param , type hint , return , docstring, * , /, logic]
lambda   [param , logic , liner code]
if       True if condition else False
list comprhension      [i if  for i in iterable if filter_condition]
dict comprhension      {i:v for i , v in enumerate(iterable )
packing 
unpacking
"""

# name = ["John" , "Karil" , "Doe"]
# height = [180 , 200 , 165]
# d = dict(zip(height ,name ))


# strs = ["cba","daf","ghi"]
# print(sum([list(sorted(i)) != list(i) for i in zip(*strs)]))


# s = "aaab"
# c = "b"
# res = []
# for i in range(len(s)):
#     distance_left = 0
#     tmp = i
#     while 0 <= tmp and s[tmp] != c:
#         tmp -= 1
#         distance_left += 1
#     if c not in s[:i+1]:
#         distance_left = len(s)
#     distance_right = 0
#     tmp = i
#     while len(s) > tmp and s[tmp] != c:
#         tmp += 1
#         distance_right += 1
#     if c not in s[i:]:
#         distance_right = len(s)
#
#     res.append(min(distance_left , distance_right))

# print(res)


# s = "aaabbb"
#
# print("".join(sorted(s)) == s)

# rows = ['qwertyuiop' ,'asdfghjkl' ,'zxcvbnm']
# words = ["Hello","Alaska","Dad","Peace"]


# find = [word for row in rows for word in words if set(word.lower()).issubset(set(row))]
# for row in rows:
#     for word in words:
#         if set(word.lower()).issubset(set(row)):
#             find.append(word)
# print(find)


# nums1 = [1,2,2,3,1]
# nums2 = [3,2,2]

# nums1 = [1,2,2,3,1]
# nums2 = [2,2,3]
#
# print(list((Counter(nums1) & Counter(nums2)).elements()))


# print(list((Counter(nums1) & Counter(nums2)).elements()))
# print(list(chain(*[[v]*c for v , c in (Counter(nums1) & Counter(nums2)).items()])))
# s = "aa"
# dis = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# alfa = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(len(s)-1): # i=0
#     d= 0
#     for j in s[i+1:]:
#         if s[i] == j:
#             if dis[alfa.index(s[i])] != d:
#                 return True
#         d += 1
# return True
# words1 = ["leetcode","is","amazing","as","is"]
# words2 = ["amazing","leetcode","is"]
#
#
# print(sum([(r1:=words1.count(i)) == (r2:=words2.count(i)) and r1 == 1 and r2 == 1  for i in set(words1)]))


# words = [
#     "dcedceadceceaeddcedc",
#     "dddcebcedcdbaeaaaeab",
#     "eecbeddbddeadcbbbdbb",
#     "decbcbebbddceacdeadd",
#     "ccbddbaedcadedbcaaae",
#     "dddcaadaceaedcdceedd",
#     "bbeddbcbbccddcaceeea",
#     "bdabacbbdadabbbddaea"
# ]
#
# for i , v in enumerate(words):
#     words[i] = "".join(sorted(set(v)))
# s = set(words)
# print(sum([len(list(combinations(range(words.count(i)), 2))) for i in s]))


# words = ["hello", "world", "leetcode"]
# chars = "welldonehoneyr"
# summa = 0
# chars = Counter(chars)
# for i in words:
#     for v, count in Counter(i).items():
#         if chars[v] < count:
#             break
#     else:
#         summa += len(i)
# print(summa)


# nums = [-1, 1, 2, 3, 1]
# target = 2
#
# c = 0
# for i in range(len(nums)):
#     for j in nums[i+1:]:
#         if nums[i] + j < target:
#             c += 1
# print(c)

#
# hours = [0,1,2,3,4]
# target = 2
# print(sum(i >= target for i in hours))


# nums = [1, 2, 3, 4]
# s = 0
# for i in nums:
#     s += i % 3 != 0
# print(s)
#
# return sum(i % 3 != 0 for i in nums)

# nums = [10, 4, 8, 3]
# leftSum = [sum(nums[:i]) for i in range(len(nums))]
# rightSum = [sum(nums[::-1][:i]) for i in range(len(nums))]
# return [abs(leftsum[i]-rightsum[i]) for i in range(len(leftsum))]
# leftSum = [0, 10, 14, 22]
# rightSum = [15, 11, 3, 0]

# nums = [5, 4, 2, 3]
#
# nums.sort()
# res = []
# for i in range(len(nums)//2):
#     res = res + nums[2*i:2*i+2][::-1]
# print(res)


# nums = [7, 8, 3, 4, 15, 13, 4, 1]
# mini = float('inf')
# while nums:
#     mini = min((nums.pop(0) + nums.pop(-1))/2 , mini)
# print(mini)

# [nums.sort(),min([(nums.pop(0) + nums.pop(-1)) / 2 for i in range(len(sorted(nums)) // 2)])][1]

#
# nums = [6,6,0,1,1,4,6]
# nums.sort()
#
# res = []
# for i in range(4):
#     res.append(abs(nums[i] - nums[i-4]))
# print(min(res))

# nums = [5,10,1,5,2]
# k = 1
# sum_index = 0
# for i in range(len(nums)):
#     if str(bin(i)).count('1') == k:
#         sum_index += nums[i]
# print(sum(nums[i] for i in range(len(nums)) if str(bin(i)).count('1') == k))


# nums = [0,1,4,6,7,10]
# diff = 3
# l = len(nums)
# c = 0
# for i in range(l):
#     for j in range(i+1,l):
#         for k in range(j+1, l):
#             if i < j < k:
#                 if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
#                     c += 1
# print(c)

# nums = [1,2,2,1]
# k = 1
# c = 0
# for i in range(len(nums)):
#     for j in nums[i+1:]:
#         if abs(j-nums[i]) == k:
#             c += 1
# print(c)

# nums = [7,7,7,7]
# res = []
# for i in nums:
#     c = 0
#     for j in nums:
#         if i > j:
#             c += 1
#     res.append(c)
# print(res)

# print([sum(i > j for j in nums) for i in nums])


# nums = [1,2,3,4]
# res = []
# for i in range(1,len(nums)+1):
#     res.append(sum(nums[:i]))
# print(res)
# print([sum(nums[:i]) for i in range(1,len(nums)+1) ])

# sentence = "I speak Goat Latin"
# new_text = ''
# for p, v in enumerate(sentence.split(),1):
#     if v[0].lower() in 'aioue':
#         new_text += v + 'ma'+''.join(['a']*p) + ' '
#         continue
#     new_text += v[1:]+v[0] + 'ma'+''.join(['a']*p) + ' '
# print(new_text)

# sentence = "leetcode exercises sound delightful"
# s = sentence.split()
#
# for i in range(len(sentence)-1):
#     if sentence[i][-1] != sentence[i+1][0]:
#         return False
# if sentence[0] != sentence[-1]:
#     return False
# return True

# s = "110100010"

# one_len = len(max(s.split('0'), key = len))
# zero_len = len(max(s.split('1'), key = len))
# print(one_len > zero_len)

# s = "1111"
# s = list(s)
# s[1] = 0
# print(s)
# zero = s.count('0')
# one = s.count('1')
# i = 0
# while zero != one:
#     zero += -1 if zero > one else 1
#     one += -1 if zero < one else 1
#     i += 1
# print(i)


# s = "0000111"
# tmp = len(s) // 2
# r1 = '10' * tmp
# c1 = 0
# for i in range(len(r1)):
#     if r1[i] != s[i]:
#         c1 += 1
# c1 += ('1' != s[-1] if len(s) % 2 == 1 else 0)
#
# tmp = len(s) // 2
# r2 = '01' * tmp
# c2 = 0
# for i in range(len(r2)):
#     if r2[i] != s[i]:
#         c2 += 1
# c2 += ('0' != s[-1] if len(s) % 2 == 1 else 0)
# print(c2 if c1 > c2 else c1)


# a = "nwcn"
# tmp = ''
# for i in a:
#     if i in tmp:
#         print(i)
#         break
#     tmp += i
# else:
#     print(tmp)


# s = "aababcabc"
# c = 0
# for i in range(len(s)-2):
#     sub = s[i:i+3]
#     c += len(sub) == len(set(sub)):
# print(c)

# if a == b:
#     print(-1)
# if len(a) != len(b):
#     print(len(max([a , b] , key = len)))
# c = 0
# for i in range(len(a)):
#     c += a[i] != b[i]
# print(c)

# from string import ascii_lowercase
# s = "rcb34"
# stack = []
# for i in s:
#     if i.isdigit() and stack:
#         stack.pop()
#     else:
#         stack.append(i)
# print(''.join(stack))
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# for i in alpha:
#     if i not in sentence:
#         return False
# return True

# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# c = 0
# for i in words:
#     for j in i:
#         if j not in allowed:
#             break
#     else:
#         c += 1
# return c

# names = ["Mary","John","Emma"]
# heights = [180,165,170]
#
# print([i[1] for i in sorted(zip(heights, names), reverse=True)])

# import itertools


# hours = [12, 12, 30, 24, 24]
# print(list(map(lambda i: len(list(filter(lambda j: not (hours[i] + hours[j]) % 2, range(i + 1, len(hours))))), range(len(hours)))))


# class OrderedStream:
#
#     def __init__(self, n: int):
#         self.l = [''] * n
#         self.ptr = 0
#
#     def insert(self, idKey: int, value: str) -> List[str]:
#         self.l[idKey-1]= value
#         res = list(takewhile(lambda x: x != '', self.l[self.ptr:]))
#         print(res)
#         self.ptr += len(res)
#         return res


# class ParkingSystem:
#
#     def __init__(self, big: int, medium: int, small: int):
#         self.big = big
#         self.medium = medium
#         self.small = small
#
#     def addCar(self, carType: int) -> bool:
#         d = {
#             1: self.big,
#             2: self.medium,
#             3: self.small
#         }
#         res = bool(d[carType])
#         d[carType] -= 1 if d[carType] else 0
#         self.big, self.medium, self.small = d.values()
#         return res
#
#
# obj = ParkingSystem(1, 1, 0)
# print(obj.addCar(1))
# print(obj.addCar(2))
# print(obj.addCar(3))
# print(obj.addCar(1))
# print(obj.addCar(1))

# class OrderedStream:
#
#     def __init__(self, n: int):
#         self.data = [''] * n
#         self.ptr = 0

# def insert(self, idKey: int, value: str) -> List[str]:
# self.data[idKey-1]= value
# res = list(takewhile(lambda x: x != '', self.data[self.ptr:]))
# res = []
# for i in self.data[self.ptr :]:
#     if i != '':
#         res.append(i)
#         continue
#     break

# self.ptr += len(res)
# return res


# ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
# [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
#
# obj = OrderedStream(5)
# print(obj.data)
# print(obj.insert(3, "ccccc"))
# print(obj.data)
# print(obj.insert(1, "aaaaa"))
# print(obj.data)
# print(obj.insert(2, "bbbbb"))
# print(obj.data)
# print(obj.insert(5, "eeeee"))
# print(obj.data)

# class RecentCounter:
#
#     def __init__(self):
#         pass
#
#     def ping(self, t: int) -> int:
#         pass
#
#
# obj = RecentCounter()

# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]


# Linked List

# s = "tgsdh ajhsdgjahs"
# print(s.capitalize())


# nums = [1, 2, 1, 10]
# nums.sort()
# l = len(nums)
# maxi = 0
# for i in range(len(nums)-2):
#     tmp = nums[l - i - 3:l - i]
#     if tmp[0] + tmp[1] > tmp[2] and tmp[1] + tmp[2] > tmp[0] and tmp[0] + tmp[2] > tmp[1]:
#         maxi = max(maxi, sum(tmp))
# print(maxi)

# barcodes  =[1,1,1,1,2,2,3,3]
# 
# print(collections.Counter(barcodes).most_common())

# barcodes.sort()
# i = 1
# l = len(barcodes)
# while i < l:
#     j = i
#     if barcodes[i - 1] == barcodes[i]:
#         while j < l and barcodes[j] == barcodes[i - 1]:
#
#             j += 1
#         if j < l and barcodes[j] == barcodes[i - 1]:
#             barcodes[i], barcodes[j] = barcodes[j], barcodes[i]
#
#         else:
#             barcodes = barcodes[::-1]
#             i = 0
#     i += 1
#
# print(barcodes)

