# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         colSet = set()
#         posDiaSet = set()
#         negDiaSet = set()
#
#         queens = [["."] * n for _ in range(n)]
#
#         def backtrack(row, queens):
#             nonlocal res
#             if row == n:
#                 res += 1
#                 return
#
#             for col in range(len(queens)):
#
#                 posDiag = row + col
#                 negDiag = row - col
#
#                 if posDiag in posDiaSet or negDiag in negDiaSet or col in colSet:
#                     continue
#                 colSet.add(col)
#                 posDiaSet.add(posDiag)
#                 negDiaSet.add(negDiag)
#                 queens[row][col] = "Q"
#
#                 backtrack(row + 1, queens)
#
#                 queens[row][col] = "."
#                 colSet.remove(col)
#                 posDiaSet.remove(posDiag)
#                 negDiaSet.remove(negDiag)
#
#         res = 0
#         backtrack(0, queens)
#         return res
#
#
# print(Solution().totalNQueens(n=5))

# Input: intervals = [[1,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
#
#
# in_  = [[1,4],[2,3]]
#
# res = [in_[0]]
# for i in range(1 , len(in_)):
#     if res[-1][0] <= in_[i][1] and res[-1][1] >= in_[i][1]:
#         continue
#     mini = min(res[-1][0] , in_[i][0])
#     maxi = max(res[-1][1] , in_[i][1])
#
#     if cond1:= mini == in_[i][0]:
#         res[-1][0] = mini
#     if cond2:= maxi == in_[i][1]:
#         res[-1][1] = maxi
#     if not (cond1 or cond2):
#         res.append(in_[i])
#
# print(res)




