# class A:
#     def __init__(self , a):
#         self.a = a
#
# class B:
#     def __init__(self, b):
#         self.b = b
#
# class C(A , B):
#     def __init__(self, a, b, c):
#         A.__init__(self, a)
#         B.__init__(self, b)
#         self.c = c
#
# obj = C(1, 2 , 3)
# print(obj.a)
# print(obj.b)
# print(obj.c)

# dictionary
# english->uzbek
"""
input: apple olma  
input: car moshina  
input: apple nimadir 
apple olma 
input: car fura 
car moshina
"""
# d = {}
#
# while True:
#     key , value = input().split()
#     # if v:=d.get(key):
#     #     print(key , v)
#     #     continue
#     d[key] = value
#     print(d)
# d.update({key: value})
# d.update([(key , value)])



#
# class A:
#
#     def __init__(self, a, b, c):
#         self.a = a  # PUBLIC
#         self._b = b  # PROTECTED
#         self.__c = c  # PRIVATE
#
#     @property
#     def b(self):
#         return self._b

#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, val):
#         self.__c = val


# obj = A(1,2,3)
# obj.c = 10
# print(obj.c)







# obj = A(1, 2, 3)
# obj.__c = 10
# print(obj.__c)
# print(obj.c)


# class A:
#     def __init__(self , a):
#         self.__a = a
#
# obj = A(1)
# obj._A__a = 10
# print(obj._A__a)

# num = int(10)
# print(num)


# class BankAccount:
#     def __init__(self , account_number ,balance ):
#         self._account_number = account_number
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance
#
# obj = BankAccount("1234123412341234" , 50_000)


# a = (0)
# print(bool(a))

# a: list['A'] = []

# class A:
#     def __init__(self,a):
#         self.a = a

#     def save(self):
#         a.append(self.__dict__)
#         a.append(self)



# A(10).save()

# a[0] = a[0].update({"a":20})
# print(a[0].get("a"))



# a[0].a = 20
# print(a[0].a)









