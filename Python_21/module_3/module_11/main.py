# res = []
#
# class BinaryTreeNode:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
#     def insert(self, data):
#         if self.data:
#             if self.data <= data:
#                 if self.right is None:
#                     self.right = BinaryTreeNode(data)
#                 else:
#                     self.right.insert(data)
#             else:
#                 if self.left is None:
#                     self.left = BinaryTreeNode(data)
#                 else:
#                     self.left.insert(data)
#         else:
#             self.data = data
#
#
#     def printTree(self):
#         if self.left:
#             self.left.printTree()
#         print(self.data , end = " ")
#         if self.right:
#             self.right.printTree()
#
#     def inorderTree(self):
#         if self.left:
#             self.left.inorderTree()
#         res.append(self.data)
#         if self.right:
#             self.right.inorderTree()
#
#
# l = [50 , 100 , 45 , 11 ,  15 , 30 , 78]
#
# l.sort()
#
# root = BinaryTreeNode(l[0])
# for i in l[1:]:
#     root.insert(i)
#
# root.inorderTree()
# print(res)

# node1 = BinaryTreeNode(50)
# node2 = BinaryTreeNode(20)
# node3 = BinaryTreeNode(45)
# node4 = BinaryTreeNode(11)
# node5 = BinaryTreeNode(15)
# node6 = BinaryTreeNode(30)
# node7 = BinaryTreeNode(78)
# node1.left = node2
# node1.right = node7
# node2.left = node4
# node2.right = node3
# node3.left = node6
# node4.right = node5
# from math import log2
#
# print(log2(1000000000001))
#
# find = 1000000000000
# l = range(1000000000000)
# L = 0
# H = len(l)-1
# c = 0
# while L <= H:
#     c += 1
#     mid = (L + H) // 2
#     if l[mid] == find:
#         print(mid)
#         break
#     if l[mid] > find:
#         H = mid - 1
#     else:
#         L = mid + 1
# else:
#     print("Not Found")
# print(c)


# data = [4, 6, 1, 2, 9, 0, 5]
#
# for i in range(len(data)):
#     tmp = i
#     for j in range(i, len(data)):
#         if data[j] < data[tmp]:
#             tmp = j
#     data[i], data[tmp] = data[tmp], data[i]
#
# print(data)

# ============= algo 33 ===============

# x , y , z = map(float , input().split())
# maxi = max(x + y + z , x , y , z)
# mini =  min(x + y/2 , x , y , z)**2
# print(f"{maxi:.2f} {mini:.2f}")


# ============= algo 35 ===============

a , b , c = map(int , input().split())

if c <= b <= a:
    print(a * 2 , b * 2 , c * 2)

else:
    print(abs(a) , abs(b) , abs(c))

