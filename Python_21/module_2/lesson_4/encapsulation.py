# encapsulation OOP

# ================== public =====================
# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# a = A(1,2)
# print(a.a)
# a.a = 3
# print(a.a)

# JAVA , C++ -> security


# ================== protected =====================
# class A:
#     def __init__(self, a, b , balance):
#         self._a = a
#         self._b = b
#         self._balance = balance
#     @property
#     def b(self):
#         return self._b
#
#     @property
#     def a(self):
#         return self._a
#
#     @b.setter
#     def b(self, new_val):
#         self._b = new_val
#
#     @a.setter
#     def a(self, new_val):
#         self._a = new_val
#
# a = A(1,2,1_000_000)
# print(a.a)
# a.a = 500_000

# ================== private =====================
class A:
    def __init__(self, a, b , c):
        self.a = a
        self._b = b # protected
        self.__c = c # private

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @b.setter
    def b(self, new_val):
        self.__b = new_val

class B(A):
    def __init__(self ,a , b , c ):
        super().__init__(a , b , c)
    def print_show(self):
        print(f"{self.a} {self._b} {self.c}")

B(1,2,3).print_show()



# a = A(1,2)
# a1 = A(1,2)
# a2 = A(1,2)
# a3 = A(1,2)
# a4 = A(1,2)
# a5 = A(1,2)
# a6 = A(1,2)


# a._A__b = 100
# print(a._A__b)

# print(a._b)
# a.b = 10
# print(a.b)

# name mangling





