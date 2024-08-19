# print((lambda num: 'Juft' if num % 2 == 0 else "Toq")(20))
# ]
# def function_name(num):
#     return 'Juft' if num%2 == 0 else "Toq"

# print(function_name(19))

# lambda params : logic
"""
    task1:
        s = 90
        %2 and %5 -> True
        else -> False
"""
# s = 90
# f = lambda num: True if num % 2 == 0 and num % 5 == 0 else False
# print(f(s))


# l = [i for i in range(1, 10) if i % 2 == 0]
# l = ["Juft" if i % 2 == 0 else 'Toq' for i in range(1,10)]
# p = [50, 34, 12, 5, 76]
# print(sum([1 for i in p if i % 5 == 0]))
# output : 55
#
# """massiv:
#         str
#         list
#         tuple
#         set
#         dict
# """
# l = [1,2,3]
# l[0] , l[1] = l[1] , l[0]
# print(l)
#
# t = (1,2,3)
#
# s = {} # v
# d = {} # k : v


# for i in range(1, 10):
#     if i % 2 == 0:
#         l.append("Juft")
#     else:
#         l.append("Toq")
# print(l)

# names = {"John" , "Karil" , "Vashington"}
# print(names[1])

# a = "Hello world !"
# 1 - usul
# l = []
# for i in a:
#     if not i in l:
#         l.append(i)
# print(len(l))
# 2 - usul
# (l := []), [l.append(i) for i in a if not i in l] , print(len(l))

# s = {1,1,1,2,1,1,1,1,1}
# s.add(10)
# s.clear()
# print(s)
# ================
# b = s
# b.add(20)
# print(s)
# print(b)

# name.discard("karil")
# name.difference(["John" , "karil"])
# name.difference_update(["John"])
# print(name.intersection(["John"]))
# name.intersection_update(["John"])
# print(name.isdisjoint(["John1", "karil1"]))
# print(name.issubset(["John", "karil" , 1 , 4]))
# print(name.issuperset(["John", "karil"]))
# print(name.pop())
# name.remove("karil1")
name = {"John" , "karil",1,2,5}
# print(name.symmetric_difference([1,"John", "karil"]))
# name.symmetric_difference_update([1,"John", "karil"])
# print(name.union([1,2,3,4]))
# print(name.update([1, 2, 3, 4]))
# print(name)
# l = [20,40]
# l.extend([11,2,3])
# print(l)

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

# unhashable -> list, set , dict
# hashable -> int, str , bool , tuple , complex
# a = {9,2,3,4,5,6,8,1 , (1,2,3)}
# print(a)

# 9:00 - 15:00

