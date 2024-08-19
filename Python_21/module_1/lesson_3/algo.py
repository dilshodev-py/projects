"""https://algo.ubtuit.uz/problem/30"""
# from math import sqrt, e, sin
#
# x , y , z  =map(float , input().split())

# AF = 2**(-x) * sqrt(x + pow(abs(y) + 2, 1/4)) * pow(e**(x-1)/sin(z + 2) + 2, 1/3)
# print(f"{AF:.2f}")
from math import sqrt

"""https://algo.ubtuit.uz/problem/33"""
# x , y , z = map(float , input().split())
# print(f"{max(x + y + z , x , y , z):.2f} {min(x + y/2, x , y , z)**2:.2f}")


"""https://algo.ubtuit.uz/problem/34"""

# a , b , c = map(int , input().split())
# print('YES') if a < b < c else print("NO")


"""https://algo.ubtuit.uz/problem/35"""

# a , b , c = map(int , input().split())
# if c <= b <= a:
#     print(2*a , 2*b , 2*c)
# else:
#     print(abs(a) , abs(b) , abs(c))

"""https://algo.ubtuit.uz/problem/37"""

# a , b = map(int , input().split())
# (a := 0) if a <= b else (a := a)
# print(a , b)


"""https://algo.ubtuit.uz/problem/39"""

# x , y = map(float , input().split())
# print(4*x*y , (x + y)/2) if x > y else print((x + y)/2 , 4*x*y)


"""https://algo.ubtuit.uz/problem/40"""

# a = None , None , None
# x , y , z = map(int , input().split())
# print(x**2, end=' ') if x > 0 else print(x, end = ' '), print(y ** 2, end = ' ') if y > 0 else print(y, end = ' ') ,  print(z ** 2) if z > 0 else print(z)

"""https://algo.ubtuit.uz/problem/41"""

# x , y , z = map(float , input().split())
# if x < 1 and y < 1 and z < 1:
#     mini = min(x , y , z)
#     if mini == x:
#         print((y + z) / 2 , y , z)
#     elif mini == y:
#         print(x , (x + z) / 2 , z)
#     else:
#         print(x, y, (x + y) / 2)
# else:
#     print(x , y , z)


"""https://algo.ubtuit.uz/problem/45"""

# a , b , c = map(int , input().split())
# D = b ** 2 - 4*a*c

# if D >= 0:
#     x1 = (-b + sqrt(D))/(2*a)
#     x2 = (-b - sqrt(D))/(2*a)
#     print(f"{x1:.2f} {x2:.2f}")
# else:
#     print('NO')

# space -> 1 2 3 4 5 6
# space -> 0 1 2 3 4 5 6

# mutable    -> list , set , dict , tuple
# immutable  -> str , int , complex , bool , float , tuple


# a = 10
# print(id(a) ,a)
# a += 20
# print(id(a) , a)

# a = [1,2,3,4]
# print(id(a) , a)
# a.append(5)
# print(id(a) , a)

# a = (1,2,3 , [1,23])
# print(id(a) , a)
# a[-1].append(10)
# print(id(a) , a)


"""
hashable   -> int , str , float , complex , bool , tuple  -> immutable
unhashable -> list , set , dict , tuple                   -> mutable
"""
# a = [1,1,3,4,5]
# print(hash(a))

# shifr -> qaytadi
# hash  -> qaytarib bumidi


# bcrypt
# database -> manager
# username -> botir
# password -> asdfdsahjbfkjh23b4t56   xafsizmi ?


