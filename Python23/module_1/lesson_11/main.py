"""
1) dict
2) list comprehension
3) dict comprehension
"""
"""
int
float
bool
str
complex
list
tuple 
set    {iteams}
dict   {key : value}
"""

# hashable - int , float , str , complex , bool , tuple
# unhashable - list , set , tuple , dict
# d = {
#     "key1" : "any1 data type",
#     "key1" : "any2 data type",
#     "key1" : "any3 data type",
# }
# unique -> yagona
# print(len(d))
# set_ = {1,2,3,4,5,1, {1,2,3}}
# print(len(set_))

# l = ["olma" , "apelsin" , 'olcha']
# print(l[0])
# fruits = {
#     "apple" : 'olma',
#     "orange" : 'apelsin',
#     'cherry' : 'olcha'
# }

# for key in fruits:
#     print(key , "->", fruits[key])

#
#
# fruits = {
#     "apple" : 'olma',
#     "orange" : 'apelsin',
#     'cherry' : 'olcha'
# }

"""
apple -> olma
orange -> apelsin
cherry -> olcha
"""

# l = [1,2,3,4,5]
# l[1] = l[1]+8
# print(l)
# fruits = {
#     "apple" : "olma",
#     "orange" : 'apelsin',
#     'cherry' : 'olcha'
# }
# fruits['apple'] = list(fruits['apple'])
# print(fruits)

# fruits = {
#     "apple" : "olma",
#     "orange" : 'apelsin',
#     'cherry' : 'olcha',
#     'watermelon' : 'tarvuz'
# }
#
# for key in fruits:
#     fruits[key] = len(fruits[key])
# print(fruits)
# 16:15
# print(type(fruits))

# i = 1
# for key in fruits:
#     if i % 2 == 0:
#         print(fruits[key] , key)
#     else:
#         print(key , fruits[key])
#     i += 1

"""
apple olma
apelsin orange
cherry olcha
tarvuz watermelon
"""

# fruits = {
#     "apple" : "olma",
#     "orange" : 'apelsin',
#     'cherry' : 'olcha',
#     'watermelon' : 'tarvuz'
# }

# copy_dict = fruits.copy()
# for key in copy_dict:
#     fruits[len(key)] = fruits[key]
# print(fruits)

# fruits["new_val"] = "value"
# print(fruits)



# fruits = {
#     "apple" : "olma",
#     "orange" : 'apelsin',
#     'cherry' : 'olcha',
#     'watermelon' : 'tarvuz',
# }
# values = list(fruits.values())[::-1]
# i = 0
# for key in fruits:
#     fruits[key] = values[i]
#     i += 1

# for i,key in enumerate(fruits):
#     fruits[key] = values[i]
# print(fruits)



# print(fruits.keys())
# print(type(fruits.values()))
#

fruits = {
    "apple" : "olma",
    "orange" : 'apelsin',
    'cherry' : 'olcha',
    'watermelon' : 'tarvuz'
}

# l = ["a" , "b" , "c"]
# print(fruits.fromkeys(l, 0))
# print(fruits)

# print(fruits.pop("cherry"))
# print(fruits.popitem())
# print(fruits)

# fruits.setdefault("cherry", 0)
# print(fruits)

# print(fruits.get("1"))


# for key , val in fruits.items():
#     print(key , '->' , val)


# print(list(fruits.items()))

# a = fruits.copy()
# a[1] = 1
# print(fruits)
# print(a)


# fruits.clear()
# print(fruits)

# fruits.update({"lemon" :"limon" , "banana" : "banan"})
# fruits.update([("lemon" , "limon") , ("banana" , 'banan')])
# print(fruits)


# del fruits['apple']
# print(fruits.pop("apple",[1,2,3]))
# print(fruits)
"""
apple -> olma
orange -> apelsin
cherry -> olcha
watermelon -> tarvuz
"""

# print(fruits.get("1"))
# print(fruits['1'])


"""
keys
values
get
pop
update
clear
copy
items
setdefault
popitem
fromkeys
"""

# a = "11315"
#
# d = {}.fromkeys(a, 0)
# for i in a:
#     d[i] += 1
# print(d)



# a = {1:1}
# print(a.fromkeys(["a", "b", "c", "c"], 0))
# print(a)

# a = "adfsergthyjuyktiyujthtgfertyt"
# d = {}.fromkeys(a , 0)
# for i in a:
#     d[i] += 1
# print(d)














