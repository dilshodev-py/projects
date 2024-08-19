""""""
"""
id()         address
bin()        10 lik -> 2 lik      
oct()        10 lik -> 8 lik      
int()        10 lik
hex()        10 lik -> 16 lik
mutable      list , tuple , set ,dict  
immutable    int , float , str , tuple , complex , bool
packing       
unpacking
type casting "10.1" -> float -> int
type hinting a : float = 10.0
.234         0.234
1_000_0000    
memory (stack[variable] , heap[value]) id()
bool      
hashable       
unhashable

"""
# bool -> True , False , 1 , 0 , [] , (), [2] , 0.001 ,

# print(bool((0,)))
# a = (0,)   # unpacking
# print(type(a))
# print(10000000)
# a : float
# a = 10.0
# print(int(float("10.1")))
# a = 1,2,3,4,5,6  # packing
# print(a)
# a , b , c = 10 , 89 , 78 # unpacking


# def func(*args):  # packing
#     print(args)
#
# t = [1,2,3,3,4,5]
# func(*t)  # unpacking
#
#
# def func(**kwargs):  # packing
#     print(kwargs)
#
#
# d = {"n1" : 1 , "n2" : 2 , "n3" : 3 , "n4" : 4 , "n5":5}
# func(**d)  # unpacking
"""
mutable      list , tuple , set ,dict  
immutable    int , float , str , tuple , complex , bool

hashable      immutable
unhashable    mutable
"""
# a = ["10"]
# print(id(a))
# a += ["1"]
# print(id(a))
# print(hash(a))

# hash -> ortga qaytmidi
# shifr -> ortga qaytadi

# list_ = [1,1,2,2,3,4,5,6] # index , slice , bir xil qiymatli element bor , for
# print(len(list_))
# c = 0
# for _ in list_:
#     c += 1
# print(c)
# print(list_[:len(list_)//2] ,list_[len(list_)//2:] )

# a = [1,2,3].copy()
# b = [1,2,3][:]

# python -> objects
# [].append()
# [].index()
"""
clear     0    
copy      0
append    1
insert    2 (1 tasi majburiy)
extend    1 (iterable[list , str , tuple , set , dict])
pop       1 (index)
remove    1 (object)
index     3 (object)(start ,stop)
count     1 (object)
reverse   0  
sort      1 key => nimasi sort lash kereligini berasiz
"""












