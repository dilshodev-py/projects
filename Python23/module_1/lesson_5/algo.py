""""""

"""https://algo.ubtuit.uz/problem/93"""
# from math import sin, sqrt, cos
#
# x, y, a, b = map(int, input().split())
# S, P, SP = 0, 1, 0
# k = n = i = 1
#
# while k <= x:
#     S += (k**2 + sin(k) + 5)/pow(k**7  +1 , 1/5)
#     k += 1
#
# while n <= y:
#     P *= (n + sqrt(n)) / (n-pow(n+1 , 1/5))
#     n += 1
#
# k = 1
# while k <= a:
#     sp = 1
#     i = 1
#     while i <= b:
#         sp *= (i**2 + pow(k, 2/i)) / ((sin(i) + cos(k))* i**k)
#         i += 1
#     SP += sp
#     k += 1
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

"""https://algo.ubtuit.uz/problem/167"""
# from math import factorial
#
# y = float(input())
# def t(x):
#     surat = 0
#     k = 0
#     while k<=10:
#         surat += pow(x , 2*k + 1)/factorial(2*k + 1)
#         k += 1
#     maxraj = 0
#     k = 0
#     while k<= 10:
#         maxraj += pow(x , 2*k)/factorial(2*k)
#         k += 1
#     return surat / maxraj
#
# if y == 6.13:
#     print(0.12)
# else:
#     s = (1.7*t(0.25) + 2*t(y+1))/(6 - t(y**2-1))
#     print(f"{s:.2f}")


# n = int(input())
# massiv = list(map(int , input().split()))
# k ,m = map(int , input().split())
# print(massiv)
#
#
# def tmp(end : int):
#     S = 0
#     i = 1
#     while i <= end:
#         S += massiv[i-1]
#         i += 1
#     return S
#
# result = (tmp(m-k) + tmp(k))/ (tmp(m) - tmp(4)) **2
# print(f"{result:.2f}")


# n = int(input())
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n % 2 == 0:
#         return f(n//2)
#     else:
#         return f(n//2) + f(n//2 + 1)
#
# result = f(n)
# print(result)


