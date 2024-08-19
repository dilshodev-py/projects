# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# n = 4 # row
# m = 4 # col
# matrix = []
# tmp = 1
# for i in range(n):
#     l = []
#     for j in range(m):
#         l.append(tmp)
#         tmp += 1
#     matrix.append(l)
# print(*matrix , sep='\n')


# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# m[2][1] = 20
# print(*m , sep='\n')

# 16:10


# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# f = []
# for i in m:
#     j = [i[-1]] + i[1:-1] + [i[0]]
#     f.append(j)
# print(f)

# print(*[[i[-1]] + i[1:-1] + [i[0]] for i in m] , sep='\n')


# m = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# m[0][0] , m[-1][-1] , m[-1][0] , m[0][-1] = m[-1][-1] , m[0][0]  , m[0][-1] , m[-1][0]
# print(*m, sep='\n')


# matrix = [
#     [3, 7, 8],
#     [9, 11, 13],
#     [15, 10, 17]
# ]
# for i in zip(*matrix):
#     i = list(i)
#     in_ = i.index(max(i))
#     if max(i) == min(matrix[in_]):
#         print([max(i)])
#         break
# else:
#     print([])



