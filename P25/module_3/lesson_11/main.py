# class TreeNode:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = TreeNode(data)
#                 else:
#                     self.left.insert(data)
#             else:
#                 if self.right is None:
#                     self.right = TreeNode(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
#     def print(self):
#         if self.left:
#             self.left.print()
#         print(self.data, end=" ")
#         if self.right:
#             self.right.print()
#
#     def inorderTree(self, root):
#         res = []
#         if root:
#             res = self.inorderTree(root.left)
#             res.append(root.data)
#             res = res + self.inorderTree(root.right)
#         return res

# # l = [3, 8, 10, 1, -20]
# # root = TreeNode()
# # for i in l:
# #     root.insert(i)




