""""""
from math import ceil, floor

"""
TelegramCloneRivision
    - app(dir)
        - database(dir)
            - channels.txt
            - contacts.txt
            - groups.txt
            - messages.txt
            - users.txt
            
        
        - model(package)
            - __init__.py
            - channel.py
            - contact.py
            - db_control.py
            - group.py
            - message.py
            - user.py
            
        - ui(dir)
            -revision.py
            
        - utils(dir)
            -revision.py
            
    - revision.py
16:00   
"""

# class A(object):
#     def __init__(self , a , b):
#         print("Start init")
#         self.a = a
#         self.b = b

# def __new__(cls, *args, **kwargs):
#     return super(A, cls).__new__(cls)

# def __del__(self):
#     print("start del")

# a = A(1,2)
# del a
# print(a)


class A:

    def __init__(self, name):
        self.name = name
    def __ceil__(self):
        print("ceil call method")

    def __floor__(self):
        print("floor call method")
    def __abs__(self):
        print("abs call method")

    def __add__(self, other):
        return self.name + other

    def __mul__(self, other):
        return self.name * other

    # def __str__(self):
    #     return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def __hash__(self):
        return 0

    # def __ne__(self, other):
    #     return len(self.name) != other

    # def __gt__(self, other):
    #     return len(self.name)  > other


    # def __dir__(self):
    #     return ["a" , "b"]




# a = A("Botir1234567")
# print(a)
# print(hash(a))
# print(dir(a))
# print(a > 10)




    # def __len__(self):
    #     print("len call method")
    #     i = 0
    #     for _ in self.name:
    #         i += 1
    #     return i


# a = A("Botir")
# print(a * 2)


# floor(a)
# abs(a)
# print(len(a))
#
# len("Botir")
# str()


