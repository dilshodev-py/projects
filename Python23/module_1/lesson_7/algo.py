# from math import sqrt

# a, b , c = map(int , input().split())
# D = b**2 - 4*a*c

# if D >= 0:
#     x2 = (-b - sqrt(D)) / (2*a)
#     x1 = (-b + sqrt(D)) / (2*a)
#     print(f"{x1:.2f} {x2: .2f}")
# else:
#     print("NO")

# https://algo.ubtuit.uz/problem/153

# words = input().split()
# for i in words:
#     print(i , len(i))

# https://algo.ubtuit.uz/problem/154
# number = str(int(input()))
# summ = 0
# for i in number:
#     summ += int(i)
# print(summ)

# https://algo.ubtuit.uz/problem/155

# words = input().split()
# c = 0
# for i in words:
#     if i[0].isupper():
#         c += 1
# print(c)

# https://algo.ubtuit.uz/problem/156

# words = input().split()
# i , j = map(int , input().split())
# words[i-1] , words[j-1] = words[j-1] , words[i-1]
# print(" ".join(words))


# https://algo.ubtuit.uz/problem/157

# words = input().split()
# i = int(input())
# words[i-1] = "TATU"
# print(*words)

# https://algo.ubtuit.uz/problem/161

# hello = "ASSALOM"
#
# l = int(input())
# cards = input().split()
# for alpha in hello:
#     if not hello.count(alpha) <= cards.count(alpha):
#         print("NO")
#         break
# else:
#     print("YES")

# https://algo.ubtuit.uz/problem/164
# word = input()
# L, R = map(int, input().split())
#
# if L < R:
#     print(word[L - 1:R])
# else:
#     print(word[R - 1:L][::-1])







