# print(10, end=' ', sep = " ")
# print(10 , 20 , 30 , sep="|")
# print(10 , 20 , 30 , sep="|" , file=open('logs.txt','w'))
# =========================================================
# for i in range(1, 10):
#     print(i , end = ' ')

# l = [12,3,4,5,6,8]

# for space , value in enumerate(l,1):
#     print(space , value)

# i = 0
# while i < len(l):
#     print(i , l[i])
#     i += 1
# ============================================
# list comprehension
# print([(i,v) for i , v in enumerate(1, 100)])
# print([i for i in range(1, 100) if i % 2 == 0])

# ============================================
# dict comprehension
# names = ["Botir" , "Kamol" , "Qudrat"]
# print({i: v for i, v in enumerate(names)})
# for i , v in enumerate(names):
#     d[i] = v
# print(d)

# ===================================
# print(1,2,3,4,5,6,7, sep="|")
# def function_name(*args ,num2, **kwargs):
#     print(args)
#     print(num2)
#     print(kwargs)
#
# function_name(1,2,3,4,5,6,7,num2 =8 , num3 = 9)

# def a(arg1 ,/, * , arg2):
#     pass
# a( 1 , arg2 = 2)

# print((lambda arg1, arg2, arg3: (arg1 if arg1 > arg3 else arg3) if arg1 > arg2 else (arg2 if arg2 > arg3 else arg3))(8,10,20))


# =============================================

# unpacking
# a, b, c = 1, 2, 3

# packing
# d = 1,2,3,4,5,6,7


# def a(a, b, c , d): # unpacking
#     pass

# a(1,2,3,4)

# def a(*args, **kwargs): # packing
#     print(kwargs.get("num1"))
#
# a(1,2,3,num1 = 4)

# l =1,2,3,4,5,6,7
# print(*l, sep = "\n") # unpacking

# ===============================================

"""
              immutable
    int , float , tuple , complex , str , bool

                mutable
        list , tuple , set , dict
"""

# a = 10
# print(id(a))
# a += 1
# print(id(a))
# mutable

# ================================================

"""             hashable
              immutables
        
              unhashable
                mutable
"""

"""
    dict(
        key(hashable , unique) : value(any type)
    )
    """

""" 
    set(items(hashable , unique))
"""


# ================================================

"""
list 
tuple
"""
# import sys
# l = [1,2,3][-1]
# t = (1,2,3)[-1]
# for i in tuple(l):
#     pass
# print(sys.getsizeof(l))
# print(sys.getsizeof(t))


# ==========================================

# class A:
#     def __init__(self,a):
#         self._a = a
# class B(A):
#     def printt(self):
#         print(self._a)
"""
OOP (Object Oriented Programing) tamoillari
    class           maket     (self.attribute and argument)
    object          nusxa
    encapsulation   public , _protected , __private  
    inheritances    single , multilevel , multiple , heachecial , hybrt 
    polymorphism    override (python) , overload (other language)
    abstraction     maket
"""


# =======================================================
# konstruktor
# class A:
#     def __


# class A:
#     def __init__(self):
#         self.a = 10


# class A:
#     pass

"""
print()
for , while
list comprehension
dict comprehension
lambda and def
unpacking
packing
immutable
mutable
hashable
unhashable
list , tuple
*args , **kwargs
OOP tamoillari
attribute and argument
konstruktor
open()
"""

# 5 -module (sertifikat) qayta topshirish yuq
