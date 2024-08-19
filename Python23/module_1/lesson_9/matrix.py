""""""
"""
matrix -> row , col

"""

# nxn
# matrix = [
#     [1, 1, 1],
#     [1, 5, 1],
#     [1, 5, 1],
#     [1, 5, 1],
#     [1, 5, 1],
#     [1, 5, 1],
#     [1, 5, 1],
#     [1, 1, 1]
# ]

# summ = sum(matrix[0]) + sum(matrix[-1])
# print(matrix[1:-1])
# for row in matrix[1:-1]:
#     summ += row[0] + row[-1]
# print(summ)


# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i + j == len(matrix[i]) - 1:
#             print(matrix[i][j])

# for i in range(len(matrix)):
#     print(matrix[i][len(matrix)-1-i])

# summ = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == j:
#             summ += matrix[i][j]
# print(summ)
# for i in range(len(matrix)):
#     summ += matrix[i][i]
# print(summ)


# for row in matrix:
#     for col in row:
#         print(col , end = " ")
#     print()


# matrix[0][0] , matrix[-1][-1] =  matrix[-1][-1], matrix[0][0]
# print(*matrix, sep='\n')
# for i in matrix:
#     print(i)
# l = [1,2,3,4,5]
# l[0] , l[-1] = l[-1] , l[0]

# for i in matrix:
#     print(max(i))
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j] , end = ' ')
#     print()
# for i in matrix:
#     print(*i)
# print(matrix[1][0])
# print(matrix[-1][-1])


"""https://algo.ubtuit.uz/problem/130"""

# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# m = int(input())
# ls = []
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if matrix[i][j] % 3 == 0:
#             ls.append(matrix[i][j])
# summ = sum(ls)
# print(summ/len(ls))



# maxi = matrix[0][0]
# mini = matrix[0][0]
# for row in matrix:
#     maxi = max(max(row) , maxi)
#     mini = min(min(row) , mini)
#     print(sum(row) , end = " ")
# print()
# print(maxi , mini)

"""https://algo.ubtuit.uz/problem/137"""

"""https://algo.ubtuit.uz/problem/143"""

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# for row in matrix:
#     print(*sorted(row))

# n, m = map(int, input().split())
# for i in range(n):
#     print(*sorted(map(int, input().split())))

