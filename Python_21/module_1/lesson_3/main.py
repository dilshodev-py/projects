"""
types in python

int          1 2 3 4 5 , int(10.5)
float        10.0 , 19.6 , 29.0 , 11,   float(11)
str          """ """ , '''''' , '' , "" , str(10)
bool         True, False ,  0 , 1, [] , [''] , (0,) , bool([])
complex      num + j , complex(10)
list         [] , list((1,2,3,4))
tuple        () , tuple([1,2,3,4])
set          {1,2,3,4,5} , set()
dict         {key : value , key2 : value2} , dict()
"""
from math import log

"""
memory : stack and heap

stack -> variable
heap  -> value
"""

"""
unpacking -> a , b , c = (1,2,3)
packing   -> a = 1, 2, 3, 4
"""

"""
builtin function
id(obj)     -> memory address
bin(num)    -> 2 lik ga o'tadi
oct(num)    -> 8 lik ga o'tadi
hex(num)    -> 16 lik ga o'tadi
int(hex(num) , 16)
input()     -> kiruvchi qiymatlari
abs()       -> module 
pow()       -> daraja
sum(massiv) -> yig'indi 10
min(massiv) -> eng kichik sondi qaytaradi
max(massiv) -> eng kotta sondi qaytaradi
map()       -> itemlarni larni bir xil typega o'tkazish
print()     -> chop etish
type()      -> objni turini qaytaradi
len()       -> uzunlikni qayatradi
"""


"""
if cond:
    body
elif cond:
    body
....

else:
    body
"""

"""
operators
*
+
-
/
//
%
**

=
+=
-=
%=
**=
/=
//=
*=

>
<
==
!=
>=
<=


and 
or 
not

10 & 3
11 | 2
20 << 2
20 >> 2
30 ^ 2

obj is obj
obj is not obj
"""
# n = int(input())
# print(bool(n & 1))

# print(10 % 2 == 0)
# print(11 & 1)

# print(bin(11))
# print(bin(1))
# 1011
# 0001
# 0001 -> 1
# ALGO -> p17 , p18

# ===================== FOR ==================

# massiv = input().split()
# summ = 0
# for i in massiv:
#     summ += int(i)
#     if summ > 10:
#         break
# else:
#     print("Finished for !")
#
# print(summ)


# massiv = list(map(int , input().split()))
# maxi  = massiv[0]
# for i in massiv[1:]:
#     print(i , end=' ')
#     (maxi := i) if maxi < i else (maxi := maxi)
# print(maxi)


# massiv = (4, 6, 9 ,10)
# summ = 0
# for i in massiv:
#     summ += i
# print(summ)


# import random
# print(random.randrange(1, 3))
# print(random.random())
# massiv = (4, 6, 9, 10)
# # 0 - 4 - 6 + 9 - 10 = 9
# i = 0
# while i < len(massiv):
#     if i == 5:
#         break
#     print(massiv[i])
#     i += 1
# else:
#     print("Finished while")



# n = int(input())
# S , i = 0 , 1

# while i <= n:
#     S += 1/i
#     i += 1
# print(S)

a , b , c , d = map(int , input().split())
S , P , SP = 0  , 1,  0
m , k  , i = 1 , 1 , 1

while m <= a:
    S += (3*m**3 + 4*m+5)/(m**3+log(m))
    m += 1
while k<= b:
    P *= k/(k**3+7*k+5)
    k += 1


while i <= c:
    sp = 1
    m = 1
    while m <= d:
        sp *= (log(i) + m**i)/m**i
        m += 1
    SP += sp
    i += 1

print(f"{S:.2f} {P:.2f} {SP:.2f}")

# codewars
# leetcode




























