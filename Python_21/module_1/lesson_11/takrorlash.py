# python module

# str   -> "" , '' , """""" , '''''', str()
#     str : immutable , hashable , "hello"
# int   -> -inf , +inf , butun(-1,1,2,3,4,5) , int()
#       int : immutable  , hashable , 987
# float -> -inf , +inf , haqiqiy sonlar(9.0, 1.5)
#       float : immutable , hashable , 654.8

# list  -> [] , list()
#         list: mutable , unhashable , [1,4,True]

# tuple -> () , (val,) , tuple()
#          tuple : immutable , hashable , (8,3,6)

# set   -> {args}, set()
#            set : mutable , unhashable , {1,2,3,4}
#            feature : shuffle , unique , methods

# dict  -> {} ,{key : value}
#             dict : mutable , unhashable , {1:1 , 2:2 , 3:3}
#
# unpacking
# packing
#
# hashable
# unhashable
#
# mutable
# immutable
#
# memory
# built-ing function

# a = "hello"
# print(a[::-1].replace('l', 't', 1)[::-1])


# a = "987.9"
# print(int(float(a)))

# a = 2/2
# print(a)


# a = (10)
# print(type(a))

# l = ["a" , " b" , " c" , "d" , "e" , [4,3,5]]   # dict = {0:"a" , 1:"b"}
# l[2] = "6"
# print(id(l))
# d = l[-1]
# print(id(d) , d)
# d.append(10)
# print(l)
# print(d)
# l = ["a" , "b" , "c" , "d" , "e"]
# for i in range(len(l)):
#     if not ord(l[i]) % 2:
#         l[i] = "0"
# print(l)

# l = ["a" , "b" , "c" , "d" , "e"]
# for index , val in enumerate(l):
#     if not ord(val) % 2:
#         l[index] = "0"

# t = (8,3,6) # size
# l = [8,3,6] # size +24

# t = (8,3,6,[8,9,6])
# t[-1][1] , t[-1][2] = t[-1][2] , t[-1][1]
# print(t)
# list out of range
# t = ("a" , "b" , "c" , "d" , "e" , "g")
# for i in range(len(t)//2):
#     print(t[i] , t[-i-1])
# if len(t) % 2:
#     print(t[len(t)//2])

# for i in range(0, len(t)-1 , 2):
#     print(t[i] , t[i+1])
# if len(t) % 2:
#     print(t[-1])

# for i in range(1 ,len(t)):
#     print(t[i-1], t[i])

# d = {1:1 , 2:2 , 3:3}
# for key , val in d.items():
#     print(key , val)

# d[1] , d[3] = d[3] , d[1]
# print(d)


# d = [
#     {
#         "id": 1,
#         "product_name": "Iphone 15 pro MAX",
#         "price": "1800$",
#         "count": 10,
#         "color": ["RED", "BLACK", "GRAY", "GOLD", "WHITE"]
#     },
#     {
#         "id": 2,
#         "product_name": "Iphone 14 pro MAX",
#         "price": "1000$",
#         "count": 20,
#         "color": ["RED", "BLACK", "GRAY", "GOLD", "WHITE"]
#     }
# ]

# print({i:i for i in [1, 2, 3]})


# c = 0
# for i in d:
#     if i.get("product_name").lower().startswith("Iphone 14".lower()):
#         i["count"] -= 1
        # i["color"].append("BLUE")
    # c += i.get("count")
# print(d[1])

# d = {}
# input = "asdfghytresda"
# for i in input:
#     d[i] = d.get(i , 0) + 1
# print(*d.items() , sep ="\n")

# a(2)
# s(2)
# d(2)
# f(1)
# ......


