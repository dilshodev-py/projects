# """
# OOP
# inhertance     -> single , multiple, multilevel, hybrid,hearchical
# abstraction    -> ABC , abstractmethod
# encapsulation  -> public-'' , protected-'_', private-"__"
# polymorphizm   -> overload , overwrite
# class          -> key , object yaratish uchun
# object         -> baracha hususiyatlarni[atributes , methods]
# """
# # class A:
# #     c = 10
# #     def __init__(self, a , b):
# #         self.d = 20
# #         self.a = a
# #         self.b = b
#
# # """
# # lambda ->
# # """
# #
# # f = lambda a, b , c : (a if a > c else c) if a > b else (b if b > c else c)
# # print(f(30, 15 , 45))
#
#
# # 1 version
# # a = lambda massiv : sorted(massiv)[-1]
#
# # a = lambda massiv : ([m:=float("-inf")]+[m:=i for i in massiv if m < i])[-1]
# # print(a([70, 20, 55, 11]))
#
#
#
# #
# # class A:
# #     def __init__(self, *args):
# #         print("Init constructor")
# #         self.args = args
# #
# #
# #     def __add__(self, other):
# #         r = sum(self.args)
# #         if isinstance(other, A):
# #             return r + sum(other.args)
# #         else:
# #             return r + other
# #
# #     def __sub__(self, other):
# #         r = self.args[0] + sum([-i for i in self.args[1:]])
# #         if isinstance(other, A):
# #             return r + other.args[0]+sum([-i for i in other.args[1:]])
# #         else:
# #             return r - other
#
# # num1 = A(10,20,30)
# #
# # print(num1 - 40)
#
#
# class MyDict:
#     def __init__(self, d):
#         self.d = d
#     def __setitem__(self, key, value):
#         self.d[key] = value
#
#     def __hash__(self):
#         return 10
#
#     def __len__(self):
#         return len(self.d)
#
#     def __str__(self):
#         return f"{self.d}"
#
#     def __add__(self, other):
#         self.d.update(other)
#         return self.d

# d = MyDict({1:1})
# # print(hash(d))
# # print(len(d))
# print(d + {2: 2})






