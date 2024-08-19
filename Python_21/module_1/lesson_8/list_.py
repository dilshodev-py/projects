# # =============== list ================
# # mutable , unhashable
# # a = [item1 , item2 , item3 ....]
# import time
#
# # a = ["8" , True , [1,2,3] , (1,2) , {1:1}]
# # print(type(a) , a)
# # print(len(a))
# # print(id(a))
# # print(a[-1])
# # print(a[1:-1])
# # print(a[::-1])
# # print([1] + [2])
# # print([1] in [2 , [1]])
# # print(1 in [2 , 1])
# # print([1,2] is [1,2])
# # a = ["12"]
# # b = a
# # b += [2]
# # print(a)
# # print(b)
# # print([1,2]*10)
# # print([1,2][1]/10)
# # print([1,2] == [1,2])
#
# # a = (1,2,3)
# # print(type(a))
# # a = list(a)
# # print(type(a))
#
# # ================= methods =================
#
# # list , set , tuple , dict , str ->  iterable
# # list()
#
# # a = []
# # for i in a.__dir__():
# #     if not "_" in i:
# #         print(i)
#
#
# a = [1,2,34,1]
# print(a.count(1))   # obj
# print(a.index(1))   # obj , start , stop
# a.append(20) # [1,2,34,1,20] , [20, 1,2,34,1] , Error , None
# print(id(a) , a)
# a.insert(1, 30)
# # a += [30]
# print(id(a) , a)
# # a.extend(["123" , "123"])
# # print(a)
# # a.remove("123")
# # print(a)
# print(a.pop(2))
# print(a)
# a.clear()
# print(a)

# b = a.copy() # [:]
# a.reverse()




# a = ["a8", "a2" , "c0" , "d5"]
# a.sort(reverse=False , key = lambda x : x[-1])
# print(a)

# word = ["John3" ,"My0", "is2", "name1" ,".4"]
# word.sort(key=lambda x : x[-1])
# print(word)
# for i in word:
#     print(i[:-1] , end=' ')

# My name is John .

# l = [7,21, 2, 8, 10, 3]
# l.sort(key= lambda x : x if x % 2 == 0 else -x)
# print(l)

# a = [1,2,3,4,5,6]
# print(id(a), a)
# a[2] , a[-1] = a[-1] , a[2]
# print(id(a) , a)


# a = [10,2,3,4,5,6]
# a.append(a[0])
# a.pop(0)
# print(a)
#
# print(list(map(str, a)))

# 2 3 4 5 6 1

# l = int(input())
# iterable = list(map(int , input().split()))
# orta = sum(iterable)/l
# tmp = []
# for i in iterable:
#     if i < orta:
#         tmp.append(i)
# print(f"{sum(tmp) / len(tmp):.2f}")


# ========== 102 ===================

# n = int(input())
# massiv = list(map(int , input().split()))
# a , b = map(int , input().split())
# mini = min(massiv)
#
# for i in range(len(massiv)):
#     if a-1 <= i <= b-1:
#         massiv[i] = massiv[i]/mini + 0.0001
#
# for i in massiv:
#     print(f"{i:.1f}" , end = " ")
#


# print(f"{8.25+0.0001:.1f}")


# ========== 103 ===================
# n=int(input())
# massiv=list(map(int,input().split()))
# k,l=map(int,input().split())
# tmp=[]
# for i in range(len(massiv)):
#     if k-1<=i<=l-1:
#         tmp.append(massiv[i])
# print(f"{sum(tmp)/len(tmp):.1f}")


# n=int(input())
# massiv=list(map(int,input().split()))
# maxi = max(massiv)
# for i in range(0,len(massiv)):
#     massiv[i]=massiv[i]/maxi
# for i in massiv:
#     print(f"{i:.2f}",end=" ")

# n=int(input())
# massiv=list(map(int,input().split()))
# maxi = min(massiv)
# for i in range(0,len(massiv)):
#     massiv[i]=massiv[i]/maxi
# for i in massiv:
#     print(f"{i:.2f}",end=" ")
from math import log
#
# N = int(input())
# A = map(int, input().split())
# M = int(input())
# summ = 1
# for i in A:
#     if i > M:
#         summ *= i
# print(f"{logs(summ):.2f}")



# N = int(input())
# A = map(int, input().split())
# x , y = map(int, input().split())
# summ = 0
# for i in A:
#     if not x <= i <= y:
#         summ += 1
# print(summ)

# N = int(input())
# A = list(map(int, input().split()))
# x , y = map(int, input().split())
# summ = 0
# for i in range(len(A)):
#     if x-1 <= i <= y-1:
#         summ += A[i]**3
# print(summ)

# [21,7,3,2,8,10]

"""
count ✅
index ✅
append ✅
insert ✅
extend ✅
remove ✅
pop ✅
clear ✅
copy ✅
reverse ✅
sort ✅
"""


#
# # "10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60
#
# w = "24z6 1x23 y369 89a 900b".split()
# for i in range(len(w)):
#     for j in w[i]:
#         if j.isalpha():
#             w[i] = w[i].replace(j,"")+j
# w.sort(key = lambda x : x[-1])
#
# for i in range(len(w)):
#     w[i] = int(w[i][:-1])
#
# result = w[0]
# index = 0
# operator = "+-*/"
# for i in w[1:]:
#     if index == 4:
#         index = 0
#     result = eval(f"{result} {operator[index]} {i}")
#     index += 1
# print(round(result))
#
#
# [10 , 45 , 7 , 14 , 78 ,90 , 34]




a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
# ['5664', '3359', '2949', '9420', '4494']
for i in range(len(a1)):
    tmp=""
    for j in a1[i]:
        if j.isdigit():
            tmp+=j
    a1[i]="$"+tmp[:len(tmp)//2]+"."+tmp[len(tmp)//2:]
print(a1)




