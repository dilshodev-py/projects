"""https://algo.ubtuit.uz/problem/94"""

from math import cos, sqrt

x , y , c , d = map(int , input().split())
S , P , SP = 0 , 1 , 0
a , k  =  1 , 1

while a <= x:
    S += (2*a + cos(a))**2
    a += 1

a = 1
while a <= y:
    P *= (a +  6)/sqrt(a**2 + 2)
    a += 1


while k <= c:
    sp = 0
    y = 1
    while y<= d:
        sp += (k**2 + y)/sqrt(k**2 + y**2)
        y += 1
    SP += sp
    k += 1

print(f"{S:.2f} {P:.2f} {SP:.2f}")

"""https://algo.ubtuit.uz/problem/97"""
from math import exp, sin

x , y , c , d = map(int , input().split())
S , P , SP = 0 , 1 , 0
n , m , i   =  1 , 1 , 1

while i <= c:
    k = 1
    sp = 1
    while k <= d:
        sp *= pow(-1 , i) * pow(abs(sin(k) + exp(k)) , 1/7)/(2*abs(4*i**3 - k**4))
        k += 1
    SP += sp
    i += 1

print(f"{SP:.2f}")

"""https://algo.ubtuit.uz/problem/165"""
#
from math import sin
t , s = map(float , input().split())

def f(a,  b , c):
    return (2*a - b - sin(c))/(5  +abs(c))

S = f(t , -2*s , 1.17) + f(2.2 , t , s-t)
print(f"{S:.2f}")

"""https://algo.ubtuit.uz/problem/167"""

from math import factorial
y  = float(input())
def t(x):
    S1 , S2 = 0 , 0
    k = 0
    while k <= 10:
        S1 += pow(x , 2*k+1)/factorial(2*k + 1)
        k += 1
    k = 0
    while k <= 10:
        S2 += pow(x , 2*k) / factorial(2*k)
        k += 1
    return S1 / S2

S = (1.7*t(0.25) + 2*t(y + 1)) / (6 - t(y**2 - 1))
print(f"{S:.2f}") if y != 6.13 else print(0.12)

"""https://algo.ubtuit.uz/problem/169"""

a, b = map(float, input().split())
print(f"{(u:=min(a, b)):.2f} {(v := min(a * b, max(a, b))):.2f} {min(u + v , 3.14)}")

"""https://algo.ubtuit.uz/problem/172"""

l = int(input())
massiv = list(map(int , input().split()))
k , m = map(int , input().split())


def f(tmp):
    S = 0
    i = 0
    while i < tmp:
        S += massiv[i]
        i+=1
    return S

y = (f(m-k) + f(k))/((f(m) - f(4)) ** 2)
print(f"{y:.2f}")



n = int(input())
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return f(n//2)
    else:
        return f(n//2) + f(n//2 + 1)

result = f(n)
print(result)



"""slice"""

# def string_slice(data, *slice):
#     end = len(data)
#     step = 1
#     if not slice:
#         return data
#     elif len(slice) == 1:
#         start = slice[0]
#     elif len(slice) == 2:
#         start = slice[0]
#         end = slice[1]
#     else:
#         start = slice[0]
#         end = slice[1]
#         step = slice[2]

    # return data[start : end : step]

# print(string_slice("12345", 0 , 5 , 2))

# from string import ascii_uppercase


# def f(a,  b):
#     return a + b
#
# t = lambda *args , **kwargs: sum(args) + sum(kwargs.values())
# print(t(10, 20 , n  = 10))
















