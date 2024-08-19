""""""
"""
OOP tamoillari
    class
    object
    inheritance
    encapsulation
    polymorphism
    abstraction
    
class  1
object 2  
inheritance(vorislik)
    single          parent :1    , child : 1
    multiple        parent :1    , child : 2
    multilevel      parent :1    , child : 1 , grandchild : 1
    hybrid          parent :1    , child : 2 , grandchild : 1
    hierarchical    parent :2    , child : 1
"""


# encapsulation

# class A:
#     a = 10 # class attribute
#
# a1 = A()
# a1.a = 20
# print(a1.a)

class B:
    def __init__(self, x, y , z):
        self.x = x  # public
        self._y = y  # protected
        self.__z = z  # privet
        self.balance = 0


    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, other):
        self._y = other










# getter
# setter
