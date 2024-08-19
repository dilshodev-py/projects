# ======== list =========
""""""
"""
[] , list()
l = list()
print(l)
a = [any type]
[1] + [10 , 8] = [1 , 10 , 8]
1 in [1 , 2 ] = ?
type([1,2,3])
len()
sum(map(int , [1,2,3,'5']))
l = [1,2,3,4,5,6]
l[-3]
l[1::2]
sum(map(int , list("12345")))

[1,2,3] == (1,2,3)
print([1, 2, 3] == list((1, 2, 3)))
print([1, 2, 3] is list((1, 2, 3)))

a = [1,2,3,4,5,6]
find = a.index(4)
a.pop(find)
a.insert(find , 20)
[10,40,50][-2]/2 = 20.0
[1,5,4,8,9]
15489 -> int
print(int("".join(map(str,[1,5,4,8,9]))))

"""
# a = []
# for i in a.__dir__():
#     if not "__" in i:
#         print(i)
# a = [1,2,3,4,5,6]
# a[a.index(4)] = 20
# print(a)

# bad version
# find = a.index(4)
# print(a.pop(find))
# print(a)
# a.insert(find , 20)
# print(a)

"""
clear()    []
copy()     [:] 
append(obj)   [1,2] -> [1,2,3]
insert(index , obj)   [1,2] -> [1,3,2]
extend(iterable[str , dict , list , tuple , set])
pop(index)
remove(obj)
index(obj) 
count(obj)
reverse()
sort(reverse=bool , key = )
"""
# a = [20,8, 5,87]
# [20,5,87,8]
# def tmp(x,y):
#     return str(x)[-1]
# a.sort(key = lambda x,y : str(x)[-1] )
# print(a)

"""
# print([str(i) for i in [1, 2, 3, 4, 5]])
# print(list(map(str, [1, 2, 3, 4, 5])))
# {for i in }

# print([i for i in [1, 2, 3, 4, 5] if i % 2 == 1])
# print(["00" if i % 2 == 0 else i for i in [1, 2, 3, 4, 5]])
# print(list(map(lambda x : "00" if x % 2 == 0 else x,[1, 2, 3, 4, 5])))
# print(list(filter(lambda x : x% 2 == 1,[1, 2, 3, 4, 5])))

"""

# ================== 112===============
# l = int(input())
# massiv = list(map(int , input().split()))
# mul = 1
# for i in massiv[::2]:
#     mul *= i
# print(f"{mul / sum(massiv[1::2]):.2f}")

# ================= 113 ===============================
# l = int(input())
# massiv = list(map(int , input().split()))
#
# print(f"{sum(a:=list(filter(lambda x: x < 0, massiv)))/len(a):.2f}")


# =================== 116 ====================

# l = int(input())
# massiv = list(map(lambda x : int(x), input().split()))
# #
# print(*[f"{(i/max(massiv)+.00001):.2f}" for i in massiv])
# print(*map(lambda x :f"{x/max(massiv)+.00001:.2f}", massiv ))


# ==================117=====================

# N = int(input())
# massiv = list(map(lambda x: int(x), input().split()))
# print(sum([val for i, val in enumerate(massiv,1) if i%2==1 ]))
# print(sum([massiv[i] for i in range(len(massiv)) if (i+1)%2==1 ]))


# l = ["bir" , "ikki" , "uch" , "to'rt"]
#
# for i , val in enumerate(l,1):
#     if i % 2 == 1:
#         print(val)

# ================== 118 =================


# l = int(input())
# m = map(int, input().split())
# print(f"{sum(a:=[i for i in m if i % 2 == 1])/len(a)+.00001:.2f}")

# ==================120==================


# l = int(input())
# massiv = list(map(int , input().split()))
# x , y = map(int , input().split())
# print(len([i for i in massiv if not x <= i <= y]))

# ================== 121 ================

# l = int(input())
# massiv = list(map(int , input().split()))
# M = int(input())
# print(sum(massiv[M:]))


# ======================122 ===============


# l = int(input())
# massiv = list(map(int , input().split()))
#
# print(f"{sum([i ** 2 for i in massiv])}\n{sum(massiv)/l:.2f}")

# ======================123 ===============
# l = int(input())
# massiv = list(map(int , input().split()))

# input()
# l = list(map(int, input().split()))
# summa = sum(l[1::2])
#
#
# print(*[f'{i / summa:.2f}' if i % 2 and i > 0 else f'{i:.2f}' for i in l])
# for i in l:
#     if i % 2 and i > 0:
#         print(f'{i / summa:.2f}', end=' ')
#     else:
#         print(f'{i:.2f}', end=' ')


# ==================== 124 =======================


# l = int(input())
# massiv = list(map(int , input().split()))
# k = int(input())-1
# k_el = massiv[k]
# maxi = max(massiv)
# for i , val in enumerate(massiv):
#     if val == maxi:
#         massiv[i] = k_el
# massiv[k] = maxi
# print(*massiv)



