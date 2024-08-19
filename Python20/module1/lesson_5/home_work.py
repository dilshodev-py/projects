# from math import factorial

# y = float(input())

# def t(x):
#     k = 0
#     surat = 0
#     maxraj = 0
#     while k <= 10:
#         surat += pow(x , 2*k+1)/factorial(2*k+1)
#         maxraj += pow(x , 2*k)/factorial(2*k)
#         k += 1
#     return surat/maxraj
# if not y == 6.13:
#     s = (1.7 * t(0.25) + 2 * t(y+1))/(6 - t(y**2-1))
#     print(f"{s:.2f}")
# else:
#     print(0.12)


# https://algo.ubtuit.uz/problem/170


# s , t = map(float , input().split())
#
# def h(a , b):
#     result = a/(b**2+1) + b/(a**2+1) - pow(a-b , 3)
#     return result
#
# p = h(s,  t) + max(h(s - t , s*t), h(s - t , s+ t)) + h(1,1)
#
# print(f"{p:.2f}")

# https://algo.ubtuit.uz/problem/172
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
from math import sqrt

x , y , c ,d = map(int , input().split())
SP = 0
m , n = 1, 1

while m <= c:
    sp = 1
    while n <= d:
        sp *= sqrt(abs(m**n - n ** m)/(m**n+n**m))
        n += 1
    SP += sp
    m += 1
    n = 1
print(f"{SP:.2f}")






