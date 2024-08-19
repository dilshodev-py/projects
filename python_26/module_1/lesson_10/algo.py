# ================= https://algo.ubtuit.uz/problem/130

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# maxi = float('-inf')
# mini = float('inf')
# for i in matrix:
#     maxi = max(max(i) , maxi)
#     mini = min(min(i) , mini)
#     print(sum(i) , end = " ")
# print()
# print(maxi, mini)

# n, m = map(int, input().split())
# maxi,mini = float("-inf") , float("inf")
# for _ in range(n):
#     row = list(map(int, input().split()))
#     maxi , mini = max(maxi,max(row)) , min(mini,min(row))
#     print(sum(row) , end = " ")
# print()
# print(maxi , mini)


# ================= https://algo.ubtuit.uz/problem/131
#
# n, m = map(int, input().split())
# maxi,mini = float("-inf") , float("inf")
# matrix = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     maxi = max(maxi, max(row))
#     mini = min(mini, min(row))
#     matrix.append(row)

# for i in range(m):
#     summa = 0
#     for j in range(n):
#         summa += matrix[j][i]
#     print(summa , end = " ")

# for col in zip(*matrix):
#     print(sum(col) , end = " ")
#
# print()
# print(maxi , mini)


# ================= https://algo.ubtuit.uz/problem/132

# int(input())
# massiv = list(map(int, input().split()))
# n , m = map(int, input().split())
# massiv.extend([0]*(n*m - len(massiv)))
# [print(*massiv[i * m:i * m + m]) for i in range(n)]

# 1 - 172
# 100








