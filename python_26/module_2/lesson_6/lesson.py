# class Test:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def function1():
#         return 10 + 20
#
#     @property
#     def function2(self):
#         return 10
#
#     @classmethod
#     def from_str(cls , data : str):
#         return cls(*list(map(int , data.split(','))))
#
#     @classmethod
#     def from_list(cls , data : list):
#         return cls(*data)
# from dataclasses import dataclass
#
#
# class Test1:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#
# @dataclass
# class Test2(Test1):
#     a: int = None
#     b: int = None
#     c: int = None
#
#     def __str__(self):
#         return f"{self.a} | {self.b} | {self.c}"
#
#     def __repr__(self):
#         return self.__str__()
#
#
# print(Test2().__class__.__name__.lower())
# print(Test2(1,2,3).__dict__)
# print(Test2(1,2,3))


# class T:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return T(self.x + other.x, self.y + other.y)
#
#     def __gt__(self, other):
#         return self.x > other.x

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __len__(self):
#         return 0



