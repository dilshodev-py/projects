string = "absdd"
# print(len(set(string)))


# d = {}.fromkeys(string, 0)
# d = {}
# for i in string:
#     d[i] = d.get(i, 0) + 1
# print(*d.items(), sep='\n')

# points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

# print(max((points:=sorted(points))[i][0] - points[i-1][0] for i in range(1,len(points))))


# hours = [5,1,4,2,2]
# target = 6
#
# print(sum(map(lambda x : x >= target , hours)))


# grid  = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# matrix = []
# for i in range(len(grid)-2):
#     row = []
#     for j in range(len(grid[0])-2):
#         maxi = float('-inf')
#         for k in range(3):
#             maxi = max(maxi , max(grid[i+k][j:j+3]))
#         row.append(maxi)
#     matrix.append(row)
# print(matrix)


# board = [
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     ["p", "p", ".", "R", ".", "p", "B", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", "B", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."]
# ]
# output : 3, 3
# row, col = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 'R'][0]
# row_list = board[row]
# col_list = list(zip(*board))[col]
# row_string = "".join(row_list).replace(".", '')
# col_string = "".join(col_list).replace(".", "")
# print(row_string.count("Rp") + row_string.count("pR")+col_string.count("Rp") + col_string.count("pR"))


# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# result = []
# for i in set(arr):
#     result.append(arr.count(i))
# print(len(set(result)) == len(set(arr)))
# print(len(set([arr.count(i) for i in set(arr)])) == len(set(arr)))

# nums = [3,2,3,4,2]

# print([len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))])

