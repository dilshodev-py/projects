import json
from collections import namedtuple

import json




# class BookDTO:
#     def __init__(self , id , title , direction , author):
#         self.id = id
#         self.title = title
#         self.direction = direction
#         self.author = author

# Data Transfer Object
# with open("books.json" , "r") as f:
#     books = json.load(f)
# BookDTO = namedtuple("BookDTO" , books[0].keys())

# for i in books:
#     b = BookDTO(**i)

# d = {
#     "name": "name 2",
#     "price": 54,
#     "color": "color 2",
#     "term": "2023-01-01",
#     "id": "2"
# }
# print(d.keys())
#
# palindrome = "aba"
# palindrome_l = list(palindrome)
# for i , val in enumerate(palindrome_l):
#     if val != "a":
#         palindrome_l[i] = "a"
#         if "".join(palindrome_l) != "".join(palindrome_l[::-1]):
#             break
#         else:
#             palindrome_l[i] = val
# else:
#     if (len(set(palindrome_l)) == 1 and set(palindrome_l).pop() == "a") or palindrome_l == list(palindrome):
#         palindrome_l[-1] = "b"
#     else:
#         palindrome_l[0] = "a"
#
# print("".join(palindrome_l))





# events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
#
# events_s = sorted(events,key= lambda x: sum(x) )
# for i, val in enumerate(events_s):
#     if val[0] == val[1]:
#         if events_s.count(val) > 1:
#             del events_s[i]
# tmp = [events_s[0][0]]
# for i in events_s[1:]:
#     for j in range(i[0] , i[1]+1):
#         if not j in tmp:
#             tmp.append(j)
#             break
#
# print(tmp)
# print(len(tmp))


print(*sorted(
    [[6, 6], [3, 4], [22, 26], [29, 32], [8, 10], [8, 9], [30, 30], [19, 21], [30, 34], [20, 20], [29, 32], [4, 5],
     [16, 17], [3, 3], [14, 16], [9, 10], [2, 5], [7, 11], [3, 3], [18, 20], [26, 28], [15, 19], [26, 27], [22, 22],
     [2, 3], [16, 20], [2, 3], [23, 27], [25, 28], [17, 20]], key=lambda x : x[1]-x[0]), sep="\n")















# with open("books.json" , "r") as f:
#     data = json.load(f)
#
# books = []
# for key , value in data.items():
#     books.append(BookDTO(**value))
#
#
# for i in books:
#     if i.id == 2:
#         print(i.id)
#         print(i.title)


