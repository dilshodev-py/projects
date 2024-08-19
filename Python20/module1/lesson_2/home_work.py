

# https://algo.ubtuit.uz/problem/33


# x , y , z = map(float , input().split())
#
# print(f"{max(x + y + z, x, z, y):.2f} {min(x + y/2, x, z, y)**2:.2f}")


# https://algo.ubtuit.uz/problem/34


# a , b , c = map(int , input().split())
# if a < b < c:
#     print('YES')
# else:
#     print("NO")


# https://algo.ubtuit.uz/problem/35

# a , b ,c = map(int , input().split())
#
# if c<=b<=a :
#     print(a*2 , b*2 , c*2)
# else:
#     print(abs(a), abs(b) , abs(c))

# https://algo.ubtuit.uz/problem/38


# x , y ,z = map(float , input().split())
#
# if 1 <= x <= 3 :
#     print(x, end= ' ')
# if 1 <= y <= 3:
#     print(y ,end=' ')
# if 1 <= z <= 3:
#     print(z, end= ' ')


# https://algo.ubtuit.uz/problem/39

# x , y = map(int, input().split())
#
#
# if x != y:
#     if x > y:
#         print(f"{x * y * 4:.1f} {(x+y)/2:.1f}")
#     else:
#         print(f"{(x+y)/2:.1f} {x * y * 4:.1f}")


# https://algo.ubtuit.uz/problem/40


# x , y ,z = map(int , input().split())
#
# if x > 0:
#     x = x*x
#
# if y > 0:
#     y = y*y
#
# if z > 0:
#     z = z*z
# print(x,  y , z)


# https://algo.ubtuit.uz/problem/41

# x , y ,z = map(float , input().split())
#
# if x < 1 and y < 1 and z < 1:
#     min_ = min(x , y , z)
#     if min_ == x:
#         x = (y+z)/2
#     elif min_ == y:
#         y = (z + x)/2
#     elif min_ == z:
#         z = (x + y)/2
#     print(x , y , z)
# else:
#     print(x , y , z)


# https://algo.ubtuit.uz/problem/42

# a, b , c , d= map(float , input().split())
#
# if a <= b<=c<=d:
#     max_ = max(a , b , c , d)
#     print((str(max_) + " ") * 4)
# else:
#     min_ = min(a , b, c , d)
#     print((str(min_)+" ")*4)


# https://algo.ubtuit.uz/problem/43

# x , y= map(float , input().split())
#
# if x < 0 and y < 0:
#     x = abs(x)
#     y = abs(y)
# elif x * y < 0:
#     x = x + 0.5
#     y = y + 0.5
#
# print(x,  y)

# https://algo.ubtuit.uz/problem/44

# x , y , z= map(int , input().split())
#
# if x + y > z and y + z > x and x + z > y:
#     print('YES')
# else:
#     print('NO')

# https://algo.ubtuit.uz/problem/45
# from math import sqrt
#
# a , b , c = map(int , input().split())
#
# D = b**2 - 4*a*c
#
# if D > 0 and a !=0:
#     x1 = (-b+sqrt(D))/(2*a)
#     x2 = (-b-sqrt(D))/(2*a)
#     print(f"{x1:.2f} {x2:.2f}")
# elif D == 0 and a != 0:
#     x = f"{-b / (2 * a):.2f}"
#     print(x , x)
#
# else:
#     print('NO')


"abc"
"abc abca abcab abcabc bca bcab bcabc cab cabc abc"

# a = "aaabc"
# c = 0
# i , j = 0 , 0
# d = {"a": 0, "b":0 , "c":0}
# while i < len(a) and j < len(a):
#     d[a[j]] += 1
#     while d["a"] and d["b"] and d["c"]:
#         c += len(a) - j
#         d[a[i]] -= 1
#         i += 1
#     j += 1
# print(c)
#
# nums = [1,2,3]
#
# k = 3
# d = dict()
# for i in nums:
#     d[i] = d.get(i, 0) + 1
# c = 0
#
# for key , count in d.items():
#     if d.get(k-key):
#         if k % 2 == 0 and k-key == k//2:
#             c += d[k-key]//2
#             d[key] = 0
#             d[k - key] = 0
#         else:
#             c += min(d.get(k-key) , count)
#             d[key] = 0
#             d[k-key] = 0
# print(c)

   # 0123456
s = "ABAB"
k = 2
d = {}



























