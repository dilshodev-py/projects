# ================= 61 ===================
# from math import sin
#
# n = int(input()) # 10
# S = 0
# for i in range(1 , n+1):
#     S += sin(i)/2**i
# print(f"{S:.2f}")

# ================= 63 ===================
# from math import factorial
#
# n = int(input()) # 10
# S = 0
# i = 1
# while i  <= n:
#     S += pow(-1 , i-1)/factorial(2*i-1)
#     i += 1
#
# print(f"{S:.4f}")

# ================= 65 ===================

# n, x = map(int, input().split())
# S = 0
#
# for i in range(1 , n+1):
#     S += i/pow(x , 2*i)
# print(f"{S:.3f}")

# ================= 73 ===================


# n , x = map(int , input().split())
# S = 0
#
# for i in range(1 , n+1):
#     S += pow(x , 2*i-1)/(2*i-1)
#
# print(f"{S:.3f}")

# ================= 75 ===================
# from math import factorial
#
# n , k = map(int , input().split())
# S = 0
# i = 0
# while i<= n:
#     S += pow(-1 , i) * k**i/factorial(i)
#     i += 1

# for i in range(n+1):
#     S += pow(-1 , i) * k**i/factorial(i)

# print(f"{S:.3f}")

# ================= 77 ===================
# from math import cos, sin
#
# a, b, c, d = map(int, input().split())
# S = 0
# h = 2
# x = c
# while x <= d:
#     S += pow((sin(a * x) + pow(b, 2 * c)) / (b ** 2 + cos(x) ** 2), 1 / 3) - sin(x ** 2) / (a * b)
#     x += h
#
# # for x in range(c, d + 1, 2):
# #     S += pow((sin(a * x) + pow(b, 2 * c)) / (b ** 2 + cos(x) ** 2), 1 / 3) - sin(x ** 2) / (a * b)
#
#
# print(f"{S:.2f}")

# ================= 79 ===================
# from math import pi , cos
# a = int(input())
# h = pi/19
# x = -pi/2
# S = 0
# while x <= pi:
#     S += pow(a , a/3) + x**2*cos(a*x)
#     x += h
# print(f"{S:.2f}")

# ================= 91 ===================
# from math import log
# a, b, c, d = map(int, input().split())
# S = 0
# P = 1
# SP = 0
# for m in range(1 , a+1):
#     S += (3*m**3 + 4*m + 5) / (m**3 + log(m))
#
# for k in range(1 , b+1):
#     P *= k/(k**3 + 7*k +5)
#
# for i in range(1  , c+1):
#     sp = 1
#     for m in range(1, d+1):
#         sp *= (log(i) + m**i)/m**i
#     SP += sp
# print(f"{S:.2f} {P:.2f} {SP:.2f} ")

# ================= 100 ===================

# from math import sqrt
# x , y , c , d = map(int , input().split())
# SP = 1
#
# for i in range(1 , c+1):
#     sp = 1
#     for j in range(1 ,  d+1):
#         sp *= (i*j+y*x)/sqrt((j*x + y)**i)
#     SP *= sp
# print(f"{SP:.2f}")

# print(10, end=' ')
# print(20, end = ' ')
# print(30)
#
#
# i = -1
# while i <= 10:
#     i += 1
#     if i == 3 or i == 5:
#         continue
#     print(i)

# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# else:
#     print("finally")


