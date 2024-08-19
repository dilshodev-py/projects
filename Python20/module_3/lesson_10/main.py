#
# class Node:
#     def __init__(self , data= None , next = None):
#         self.data = data
#         self.next = next
#
#
# class Solution:
#     # def getDecimalValue(self, head: Node) -> int:
#         # str_ = ''
#         # tmp = head
#         # while tmp:
#         #     str_ += str(tmp.data)
#         #     tmp = tmp.next
#         # return int(str_ , 2)
#     # def isPalindrome(self, head: Node) -> bool:
#     #     str_ = ''
#     #     tmp = head
#     #     while tmp:
#     #         str_ += str(tmp.data)
#     #         tmp = tmp.next
#     #     return str_ == str_[::-1]
#     def reverseKGroup(self, head: Node, k: int):
#         l = []
#         tmp = head
#         while tmp:
#             l.append(tmp.data)
#             tmp = tmp.next
#
#         for i in range(0, len(l), k):
#             if len(l[i: i + k]) == k:
#                 l[i: i + k] = l[i: i + k][::-1]
#
#         head = Node(l[0])
#         tmp = head
#         for i in l[1:]:
#             tmp.next = Node(i)
#             tmp = tmp.next
#         return head
#
#
# l = [1,2,3,4,5]
# head = Node(l[0])
# tmp = head
# for i in l[1:]:
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# print(Solution().reverseKGroup(head,3))

"""
data structure
    list
    tuple
    set
    dict
    UserList
    UserDict
    namedTuple
    LinkedList
    Tree (recursive function)
"""
# res = []
# class NodeTree:
#     def __init__(self , data = None):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def insert(self , data):
#         if self.data:
#             if self.data <= data:
#                 if self.right is None:
#                     self.right = NodeTree(data)
#                 else:
#                     self.right.insert(data)
#             else:
#                 if self.left is None:
#                     self.left = NodeTree(data)
#                 else:
#                     self.left.insert(data)
#         else:
#             self.data = data
#
#     def rangeSumBST(self,root,low , high):
#         c = 0
#         if root:
#             c = self.rangeSumBST(root.left, low , high)
#             if low <= root.data <= high:
#                 c += root.data
#             c = c + self.rangeSumBST(root.right, low , high)
#         return c

# l = [10,5,15,3,7,13,18,1,6]
# root = NodeTree(l[0])
# for i in l[1:]:
#     root.insert(i)
#     #
#     # def printTree(self):
#     #     if self.left:
#     #         self.left.printTree()
#     #     print(self.data)
#     #     if self.right:
#     #         self.right.printTree()
#     #
#     # def inorder_list(self):
#     #     if self.left:
#     #         self.left.inorder_list()
#     #     res.append(self.data)
#     #     if self.right:
#     #         self.right.inorder_list()
#
# print(root.rangeSumBST(root,6, 10))

# graft

# n = NodeTree(12) # root
# n.insert(20)
# n.insert(8)
# n.insert(30)
# n.insert(4)
# n.inorder_list()
# print(res)









