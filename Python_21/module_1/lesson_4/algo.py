"""https://algo.ubtuit.uz/problem/63"""
# from math import factorial
#
# n = int(input())
# i = 1
# S = 0
# while i <= n:
#     S += pow(-1 , i-1) * 1/factorial(2*i-1)
#     i += 1
# print(f"{S:.4f}")
from math import cos, log, sin

"""https://algo.ubtuit.uz/problem/66"""
# from math import sin
# n , x = map(int, input().split())
# i = 1
# S = 0
# while i <= n:
#     S += pow(-1 , i-1)* sin(i*x)/i
#     i += 1
# print(f"{S:.3f}")

"""https://algo.ubtuit.uz/problem/70"""
# from math import sin, factorial
#
# n , x = map(int, input().split())
# i = 1
# S = 0
# while i <= n:
#     S += pow(-1, i-1) * pow(x , 2*i-1) / factorial(2*i-1)
#     i += 1
# print(f"{S:.3f}")

"""https://algo.ubtuit.uz/problem/75"""
# from math import sin, factorial
#
# n , k = map(int, input().split())
# i = 0
# S = 0
# while i <= n:
#     S += pow(-1 , i ) * k ** i /factorial(i)
#     i += 1
# print(f"{S:.3f}")

"""https://algo.ubtuit.uz/problem/76"""
# from math import sin, factorial, cos
#
# a , b , c  = map(int, input().split())
# x = a
# h = 3
# S = 0
# while x <= c:
#     S += pow((a*x  + b)/(b**2+cos(x)**2) , 1/3 ) - sin(x**2)/(a*b)
#     x += h
# print(f"{S:.2f}")

"""https://algo.ubtuit.uz/problem/77"""
# from math import sin, factorial, cos
#
# a , b , c , d  = map(int, input().split())
# x = c
# h = 2
# S = 0
# while x <= d:
#     S += pow((sin(a*x) + b**(2*c))/(b**2 + cos(x)**2), 1/3) - sin(x**2)/(a*b)
#     x += h
# print(f"{S:.2f}")

"""https://algo.ubtuit.uz/problem/79"""
# from math import sin, factorial, cos, pi
#
# a = int(input())
# x = -pi/2
# h = pi/19
# S = 0
# while x <= pi:
#     S += pow(a , a/3) + x ** 2 * cos(a*x)
#     x += h
# print(f"{S:.2f}")

"""https://algo.ubtuit.uz/problem/92"""

# x, y, a, b = map(int , input().split())
# S, P, SP = 0, 1, 0
# a1, i, k = 1, 1, 1
#
# while a1 <= x:
#     S += (a1**2 + 2*a1)/(a1**3 + a1*cos(a1)**2 + 1)
#     a1+= 1
#
# while i <= y:
#     P *= (i**2  +1)/(pow(i , 3/i) + 2)
#     i+=1
#
# i = 1
# while i <= a:
#     sp = 1
#     k = 1
#     while k <= b:
#         sp *= logs((k**i + pow(k , 1/i))/ (k**3 + pow(i, 1/k)))
#         k += 1
#     SP += sp
#     i += 1
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

"""https://algo.ubtuit.uz/problem/93"""

x, y, a, b = map(int , input().split())
S, P, SP = 0, 1, 0
k, n, i = 1, 1, 1

while k <= x:
    S += (k**2+ sin(k) + 5) / pow(k**7 + 1 , 1/5)
    k += 1

while n <= y:
    P *= (n + pow(n, 1/2)) / (n - pow(n + 1 , 1/5) )
    n+=1

k = 1
while k <= a:
    sp = 1
    i = 1
    while i <= b:
        sp *= (i**2 + pow(k , 2/i)) / ((sin(i) + cos(k)) * i**k)
        i += 1
    SP += sp
    k += 1
print(f"{S:.2f} {P:.2f} {SP:.2f}")

