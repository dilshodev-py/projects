# ====================== hierarchical =============================
# class A:
#     def __init__(self,
#                  x,
#                  y):
#         self.x = x
#         self.y = y

# class B:
#     def __init__(self,
#                  z,
#                  w):
#         self.z = z
#         self.w = w

# class C(A , B):
#     def __init__(self, x , y ,z , w , i):
#         A.__init__(self, x , y)
#         B.__init__(self, z , w)
#         self.i = i


# ====================== Multiple =============================
# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class B(A):
#     def __init__(self, x, y, z, w):
#         super().__init__(x, y)
#         self.z = z
#         self.w = w
#
#
# class C(A):
#     def __init__(self, x, y, i):
#         super().__init__(x, y)
#         self.i = i


# ============================ hybrid ===========================

"""
class
    A(a)
    B(b)
    C(c)
    D(d)
16:47
"""


# class D:
#     def __init__(self, d):
#         self.d = d
#
#
# class B(D):
#     def __init__(self, d, b):
#         super().__init__(d)
#         self.b = b
#
#
# class C(D):
#     def __init__(self, d, c):
#         super().__init__(d)
#         self.c = c
#
#
# class A(B, C):
#     def __init__(self, b, d, c, a):
#         B.__init__(self, d, b)
#         C.__init__(self, d, c)
#         self.a = a
#


# canva   -> home work
# project -> authentication

# authentication:
#     register
#     login




