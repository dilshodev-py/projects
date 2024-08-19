""""""

# class A:
#     a = 8
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(B, C):
#     pass

# class A:
#     def function(self , arg1 , arg2):
#         print(arg1 , arg2)
#
# class B(A):
#     def function(self , arg1):
#         print(arg1)
#
# b = B()
# b.function(1)
# from abc import ABC, abstractmethod
#
#
# class A(ABC):
#     def __init__(self , a):
#         self.a = a
#
#     @abstractmethod
#     def a_method(self):
#         pass
#
# class B:
#     def __init__(self , a , b):
#         super().__init__(a)
#         self.b = b
#
#     @classmethod
#     def a_method(self):
#         pass
#
# b = B(1,2)
# print(b.a)
import math

cars  = []

class Car:
    def __init__(self , name = None , model = None):
        self.name = name
        self.model = model

    @classmethod
    def from_string(cls, string_format):
        data = string_format.split(",")
        return cls(*data)


    @staticmethod
    def sequence_id():
        return cars[-1].id + 1 if cars else 1

    @property
    def info_print(self):
        print(f"{self.name} , {self.model}")

    @classmethod
    def from_tuple(cls, tuple_format):
        return cls(*tuple_format)


    def __repr__(self) -> str:
        return f"{self.name}, {self.model}"

t_format1 = ("Nexia 1" , "chevrolet")
# t_format2 = ("Nexia 2" , "chevrolet")
#
car1 = Car.from_tuple(t_format1)
# car2 = Car.from_tuple(t_format2)
# car1.info_print

# from math import pi , log
#
# pi
# log()




"""
OOP tamoillari
    class          - maket
    object         - nusxa
    inhertance     - single , multiple , multilevel , hybrid , herarhiya
    encapsulation  - public , protected , private
    polymorphism   - override(python) , overload(java)
    abstraction    - mavhumlik (classlar uchun maket)
built-in decorator - @classmethod , @staticmethod , @property
dunder method      - __init__ , __repr__ , __str__ , __class__ , __name__ , __len__(len()) , __mod__(%) , __gt__(>)  ... 
f = open(file_path , mode = [r , w , a , x])    , f.close()        
with open(file_path , mode = [r , w , a , x]) as f:
    
package directory   - __init__.py in directory
from , import       - from math import *
try / except / else / finally 
built-in Exception  
raise               print error  
library             all python file , built-in [math , string , sys , os , datetime , time , abc , .....]
structure           project [DB , model , UI , utils]
"""

# class MyException(ZeroDivisionError):
#     def __init__(self, message):
#         super().__init__(message)

# ZeroDivisionError
#     - MyException

# try:
#     raise MyException("Error")
# except ZeroDivisionError as m:
#     print(m)

# raise Exception("Not Found")




# error handling
# try:
#     n = int(input())
#     print(10/n)
# except Exception as m:
#     print(f"Error {__file__}")
#     print(f"line : {121} message: {m}")
# else:
#     print("Success !")
#
# finally:
#     print("Finished !")
