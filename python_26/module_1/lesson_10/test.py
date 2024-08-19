
# a = "dassf asdfgh adsfgh     dsfgh         sdfgdfsdgf"
# print(*a.split())


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(list(zip(*matrix)))

"""
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output : 25
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# n , m = len(matrix) , len(matrix[0])
# print(sum([matrix[i][j] for i in range(n) for j in range(m) if i == j or i + j == m-1]))
# summa = 0
# for i in range(n):
#     for j in range(m):
#         if i == j or i + j == m-1:
#             summa += matrix[i][j]
# print(summa)

"""
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
[
    (9 , 6 , 3),
    (8 , 5 , 2),
    (7 , 4 , 1),
]
"""

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(*list(zip(*matrix[::-1]))[::-1], sep='\n')



