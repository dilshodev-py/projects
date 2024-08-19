# https://algo.ubtuit.uz/problem/75
# from math import factorial
#
# n , k  = map(int , input().split())
# S = 0
# i = 0
# while i <= n:
#     S += pow(-1, i) * k ** i / factorial(i)
#     i+=1
# # for i in range(n+1):
# #     S += pow(-1 , i) * k**i/factorial(i)
#
# print(f"{S:.3f}")

# https://algo.ubtuit.uz/problem/79
# from math import pi, cos
#
# a = int(input())
# S = 0
# x = -pi/2
# h = pi/19
# while x <= pi:
#     S += pow(a , a/3) + x**2 * cos(a*x)
#     x += h
#
# print(f"{S:.2f}")

# https://algo.ubtuit.uz/problem/69
# from math import factorial
#
# n , x = map(int , input().split())
# S = 0
# i = 1
# while i <= n:
#     S += pow(-1 , i) * x**i/factorial(i)
#     i += 1
# print(f"{S:.3f}")

# https://algo.ubtuit.uz/problem/63
# from math import factorial
#
# n = int(input())
# S = 0
# i = 1
# while i <= n:
#     S += pow(-1 , i-1)/factorial(2*i-1)
#     i += 1
# print(f"{S:.4f}")

# https://algo.ubtuit.uz/problem/70
# from math import factorial
#
# n , x = map(int , input().split())
#
# S = 0
# i = 1
# while i<= n:
#     S += pow(-1 , i-1) * pow(x , 2*i - 1)/factorial(2*i - 1)
#     i += 1
#
# print(f"{S:.3f}")


# https://algo.ubtuit.uz/problem/77
# from math import sin, cos
#
# a , b , c , d = map(int , input().split())
# x = c
# y = 0
# h = 2
# while x <= d:
#     y += ((sin(a*x) +pow(b , 2*c))/(b**2+cos(x)**2))**(1/3) - sin(x**2)/(a*b)
#     x  += h
#
# print(f"{y:.2f}")

# https://algo.ubtuit.uz/problem/92
from math import cos, log10, log

x, y, a, b = map(int, input().split())

S, P, SP = 0, 1, 0
aa , i , k =1 , 1 , 1

while aa <= x:
    S += (aa**2 + 2*aa)/ (aa**3 + aa*cos(aa)**2 + 1)
    aa += 1

while i<= y:
    P *= (i**2+1)/(pow(i , 3/i) + 2)
    i += 1

i = 1
while i <= a:
    sp = 1
    while k <= b:
        sp *= log((k**i + pow(k , 1/i))/(k**3 + pow(i , 1/k)))
        k += 1
    SP += sp
    i += 1
    k = 1

print(f"{S:.2f} {P:.2f} {SP:.2f}")


