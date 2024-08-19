
# for - massiv ni uzunligiga bog'liq

# for i in range(10):
#     if i == 5:
#         print("Sikl to'xtatildi")
# else:
#     print("Sikl ohirgacha aylandi")


# c = 0
# while c < 10:
#     if c == 5:
#         print("Sikl to'xtatildi")
#     c += 1
# else:
#     print("Sikl ohirgacha aylandi")


# a = '12345678'
# b = 'hellowor'

# output:
#   'h1e2l3l4o5w6o7r8'
# s = ""
# for i in range(len(b)):
#     s += b[i] + a[i]
# print(s)
# 48-57
# "A" - 65  -> ord()
# 65 - "A"  -> chr()
# a = "(89)((90)(8)(78))"
# b = ""
# for i in a:
#     if i.isdigit():
#         b += i
#     elif len(b) != 0:
#         print(b)
#         b = ""

# a = "() (((()))())"
# l = 0
# maxi = 0
# max -> 5
# iterable -> str , list , tuple , set , dict_
# for i in a:
#     if i == "(":
#         l += 1
#     elif i == ")":
#         maxi = max(maxi , l)
#         l -= 1
# print(maxi)

# 89
# 90
# 8
# 78





# while -> else
# string
# index


# slice
# def


# def vowelStrings(words, left: int, right: int) -> int:
#     vowel = "aeiou"
#     count = 0
#     for i in words[left:right+1]:
#         if i[0] in vowel and i[-1] in vowel:
#             count += 1
#     return count
#
#
#
# words = ["hey", "aeo", "mu", "ooo", "artro"]
# left = 1
# right = 4
# print(vowelStrings(words, left, right))
from math import ceil, floor
# people = [5,1,4,2]
# limit = 6
# people.sort()
# if people[0] > limit//2:
#     print(len(people))
# else:
#     s = 0
#     c = 0
#     for i in people:
#         s += i
#         if s <= limit//2:
#             continue
#         else:
#             c += 1
#             s = i
#     print(c)

# rings = "B0B6G0R6R0R6G9"
# # 0606069
# # BBGRRRG
#
# # {
# #     0 : ['B' , 'G' , 'R'],
# #     6 : ['B' , 'G' , 'R'
# # }
# number = rings[1::2]
# color = rings[::2]
# data = {}
# for i in number:
#     data[i] = ["B", 'G', 'R']
# for i in range(len(number)):
#     if color[i] in data[number[i]]:
#         data[number[i]].pop(data[number[i]].index(color[i]))
# c = 0
# for i in data.values():
#     if  not i:
#         c += 1
# print(c)

# result = []
# print([1, 2, 3, 4] + [5, 6, 7])


# words = ["$easy$","$problem$"]
# separator = "$"
#
# result = []
# for i in words:
#     result += i.split(separator)
#
# l = []
# if '' in result:
#     for i in result:
#         if i != '':
#             l += [i]
#     print(l)
# else:
#     print(result)


# slice
# def


# iterable[start : end : step]




















