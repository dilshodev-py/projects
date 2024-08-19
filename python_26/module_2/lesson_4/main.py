# class A:
#     def __init__(self, a, b, c):
#         self.a = a  # public
#         self._b = b  # protected
#         self._b = b  # protected
#         self.__balance = c  # private
#
#     @property
#     def b(self):
#         return self._b
#
#     @b.setter
#     def b(self, value):
#         self._b = value
#


# @property
# def c(self):
#     return self.__c
#
# @c.setter
# def c(self, value):
#     self.__c = value


# a = A(1, 2, 3)
# print(a._A__balance)
# a._A__balance = 9
# print(a._A__balance)


# class B(A):
#     def __init__(self, a, b, c):
#         A.__init__(self, a, b, c)
#         super().__init__(a, b, c)
#     def add(self):
#         print(self.__c)


# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def add(self):
#         self._b


# library
# tmp = A(1, 2)
# tmp.b = 100
# print(tmp.b)


# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     @property
#     def add(self):
#         return self.num1 + self.num2


# c = Calculator(10, 89)
# print(c.add)


# class Employee:
#     def __init__(self, name, age, salary, status):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.status = status
#
#
# a = Employee('Botir', 25, 2000000, 'Developer')
# a.salary = 20000000
