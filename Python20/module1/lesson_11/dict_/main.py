# dict()
# l = ["value"]
# print(l[0])

# d = {
#     "fullname": "Botir",
#     "age": [24 , 26],
#     "address": "Toshkent",
#     "password": 1111,
# }

# d = {
    # (1, 2, 3): "tuple",
    # "1": "tuple",
    # 1.0: "tuple2",
    # 2j : "tuple"
    # (1, 2, 3): "list",
    # {1, 2, 3}: "set",
    # {1: 1, 2: 2}: "dict"
# }
# d = {
#     "fullname": "Botir",
#     "age": [24 , 26],
#     "address": "Toshkent",
#     "password": 1111,
# }

# d["address"] = "Samarqand"
# print(d)
# d["address"] =  d["password"] , d["password"]
# print(d)

# d = {
#     "fullname": "Botir",
#     "age": [24 , 26],
#     "address": "Toshkent",
#     "password": 1111
# }

# [1,2,3][1]
# print(list(d.keys())[1:])
# print(d.values())
# print(list(d.values()))

d = {
    "list1": [56 , 1],
    "list2": [24 , 26],
    "list3": [75 , 43 , 67],
    "list4": "qwer"
}
# for i in d.__dir__():
#     if not "_" in i:
#         print(i)

# r = []
# r += [56 , 1]
# r += [24 , 26]
# r += [75 , 43 , 67]
# r += ["qwer"]
# print(r)

# r = []
# for value in d.values():
#     if isinstance(value , list):
#         r.extend(value)
#     else:
#         r.extend([value])
# print(r)

# r = [56 , 1 , 24 , 26 , 75 , 43 , 67 , "qwer"]

print(d.get("list5"))
val = d.pop("list4")
# y = d.popitem()
# del d["list4"]
# print(d)
# d.update({"list1" : val , "list5" : [9, 90]})
# d.update([('list4' , val) , ("list5" , [9, 90])])
# d["list4"] = val

# d.clear()
# tmp = d.copy()
# d.setdefault("l",0)
# t = d.fromkeys("a b s s" , 0)
# print(t)
"""
get
pop
popitem
keys
values
items
update
clear
copy
setdefault
fromkeys
"""

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
#
# print(myfamily["child2"]['name'])

