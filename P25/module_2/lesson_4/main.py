# class ClassName:
#     def __init__(self , param1 , param2): # class instance attribute
#         self.name1 = param1
#         self.name2 = param2
#
#     def __repr__(self):
#         return f"{self.name1} {self.name2}"
#
# c = ClassName(1,2)
# print(c)

# a_list = []
# class A:
#     def __init__(self , a = None , b = None):
#         self.a = a
#         self.b = b
#
#     def add(self , num1 , num2):
#         return num1 + num2
#
#     def save(self):
#         a_list.append(self)

# class A:
#     def __init__(self, a, b ,c):
#         self.a = a # public
#         self._b = b # protected
#         self.__c =  c # private

# single underscore -> _
# mangle
# obj = A(10, 20 , 30)

# library
# python.org
# pip install library


# class BankAccount:
#         def __init__(self,account_card_number , balance):
#             self.account_card_number = account_card_number
#             self.balance = balance
#         def add_balace(self, summ):
#
#             self._balance += summ
#
#         def print_balance(self):
#             print(self._balance)
#
# obj1 = BankAccount("1234567843215678" , 0)

# class B:
#     def __init__(self, a, b):
#         self._a = a  # single underscore -> protected
#         self.__b = b  # dunder underscore -> private
#
#     @property
#     def a(self):
#         return self._a
#
#     @a.setter
#     def a(self, value):
#         self._a = value
# mangle
# b = B(10, 20)
# print(b.a)
# b.a = 100
# print(b.a)


# BankAccount:
#         account_holder # protected [getter]
#         balance        # private [getter , setter]


# class BankAccount:
#     def __init__(self ,account_holder , balance ):
#         self._account_holder = account_holder
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self , value):
#         self.__balance = value
#
#     @property
#     def account_holder(self):
#         return self._account_holder

# class A:
#     def __init__(self, a, b):
#         self._a = a
#         self.__b = b
#
#     def print_b(self):
#         print(self.__b)
#
#
# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def add(self):
#         return self._a + self._A__b
#
#
# print(B(10, 20).add())


# Car:
#         made
#         model
#         year
#         __km
#     drive(miles)
#     display_info()


# class Car:
#
#     def __init__(self,
#                  year,
#                  made,
#                  model,
#                  km = 0):
#         self.year = year
#         self.made = made
#         self.model = model
#         self.__km = km
#
#     @property
#     def km(self):
#         return self.__km
#
#     def drive(self , miles):
#         self.__km += miles
#
#     def display_info(self):
#         info = f"""
#             Made : {self.made}
#             Model : {self.model}
#             year : {self.year}
#             km : {self.__km}
#         """
#         print(info)

# car = Car(2000 , 'GM' , 'Chevrolet')
# print(car.km)
# car.drive(100)
# car.drive(50)
# print(car.km)
# car.display_info()






