from math import sqrt, log10, factorial

# =================== 20 ===================

# from math import cos , sin
#
# x ,  y = map(float , input().split())
#
#
# mahraj1 = x ** 2 + (x*y+y**2)/(y**2 + (y+x*y)/(abs(x*y) + 5))
# mahraj2 = 1+ cos(x) + 1/sin(abs(x))
#
# T11 = (x**2+1)/mahraj1 + 1/mahraj2
# print(f"{T11:.2f}")

# =================== 23 ===================
# from math import cos
#
# a , b , c, d , x = map(float , input().split())
#
# if a == 0:
#     print("1.00")
# else:
#     y2 = (a*x**2+b*x + c)/(x*a**3 + a**2 + a**(b-c)) + cos(abs((a*x + b)/ (c*x + d + 2 **c)))
#
#     print(f"{y2:.2f}")

# =================== 25 ===================

# a , x = map(float , input().split())
#
# TT = (sqrt(x-1) + sqrt( x+ 2) + log10(sqrt(a * x**2) + 2)) / sqrt(sqrt(x+2) + sqrt(x+24) + x**5)
#
# print(f"{TT:.2f}")

# =================== 28 ===================
# from math import sin, log10, cos
#
# a, x = map(float, input().split())
#
# BB1 = x * sin(x/2+x/3+x/4) + (log10(x**2-2) + 3**a)/(cos(x+3)*sin(x+3)+8)
# print(f"{BB1:.2f}")


# =================== 39 ===================

# x , y = map(int , input().split())


# yarim_yigindi = f"{(x + y) / 2:.1f}"
# ikilangan = f"{x * y * 4:.1f}"

# if x > y:
#     print(ikilangan , yarim_yigindi)
# else:
#     print(yarim_yigindi , ikilangan)

# =================== 38 ===================

# x , y , z = map(float , input().split())
# if 1 <= x <= 3:
#     print(x , end = " ")
# if 1 <= y <= 3:
#     print(y , end = " ")
# if 1 <= z <= 3:
#     print(z , end = " ")

# =================== 42 ===================

# a = 10
# print(f"{a}"*4)
# a, b, c, d = map(float, input().split())
#
# if a <= b <= c <= d:
#     print(f"{max(a, b, c, d)} "*4)
# else:
#     print(f"{min(a, b, c, d)} " * 4)

# =================== 44 ===================

# x , y , z = map(int , input().split())
#
# if x + y > z and x + z > y and y + z > x:
#     print("YES")
# else:
#     print("NO")

# =================== 45 ===================


# a, b, c = map(int, input().split())
#
# D = b ** 2 - 4 * a * c
#
# if D > 0:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(f"{x1:.2f} {x2:.2f}")
# elif D == 0:
#     x1 = -b /(2 * a)
#     print(f"{x1:.2f}")
# else:
#     print("NO")


# ======================== 61 ==================
# from math import sin
# n = int(input())
#
# sum = 0
# i = 1
# while i <= n:
#     sum += sin(i)/2**i
#     i+=1
#
# print(f"{sum:.2f}")

# ======================== 69 ==================


# n , x = map(int , input().split())
# S = 0
#
# for i in range(1 , n+1):
#     S += (-1)**i*x**i/factorial(i)
# print(f"{S:.3f}")


# ======================== 79 ==================
# from math import pi , cos
#
# a = int(input())
# h = pi/19
# x = -pi/2
# S = 0
# while x <= pi:
#     S += a**(a/3) + x**2*cos(a*x)
#     x += h
# print(f"{S:.2f}")

# ======================== 80 ==================

# from math import sin , cos

# a = int(input())
# h= 0.5
# x = 0
# S = 0
# while x <= 10:
#     S += a*cos(x) - sin(x**2)
#     x += h
# print(f"{S:.2f}")


# ======================== 91 ==================


# from math import log
# a , b,  c , d = map(int , input().split())
#
#
# S = 0
# m = 1
# while m<= a:
#     S += (3*m**3 + 4*m + 5)/(m**3+log(m))
#     m += 1
#
#
# P = 1
# k = 1
# while k<=b:
#     P *= k/(k**3 + 7*k + 5)
#     k += 1
#
#
# SP = 0
# i = 1
# while i <= c:
#     sp = 1
#     m = 1
#     while m<=d:
#         sp *= (log(i) + m**i) / m**i
#         m += 1
#     SP += sp
#     i += 1
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

# ======================== 92 ==================
from math import *
x, y, a, b = map(int, input().split())

A = 1
S , P , SP = 0 , 1 , 0
while A <=x:
    S += (a**2+2*a)/(a**3 + a*cos(a)**2 + 1)
    A += 1


P = 1
i = 1
while i<= y:
    P *= (i**2 + 1)/(i**(3/i) + 2)
    i += 1

SP = 0
i = 1
while i <= a:
    k = 1
    sp = 1
    while k<= b:
        sp *= log((k**i + k**(1/i))/(k**3 + i**(1/k)))
        k += 1
    SP += sp
    i += 1

print(f"{S:.2f} {P:.2f} {SP:.2f}")



"""
HOME WORK:
    algo : 1-45 and 60-100
"""


"""
READ:
    function
"""