# from typing import Optional
#
#
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
# class LinkedList:
#     def __init__(self, data):
#         self.head = Node(data)
#
#     def append(self, data):
#         tmp = self.head
#         while tmp.next:
#             tmp = tmp.next
#         tmp.next = Node(data)
#
#     def remove(self , data):
#         tmp = self.head
#         while tmp and tmp.next:
#             if tmp.next.data == data:
#                 tmp.next = tmp.next.next
#             if tmp:
#                 tmp = tmp.next
#
#
#     def insert(self , position , data):
#         tmp = self.head
#         pos = 1
#         while tmp.next:
#             if position == pos:
#                 new_node = Node(data)
#                 new_node.next = tmp.next
#                 tmp.next = new_node
#
#             pos += 1
#             tmp = tmp.next
#
#
#
#     def print(self):
#         tmp = self.head.next
#         while tmp:
#             print(tmp.data)
#             tmp = tmp.next
#
# l = [0,3,1,0,4,5,2,0]
# head = Node(l[0])
# tmp = head
# for i in l[1:]:
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# "2414"
#
#
#
#
#
# class Solution:
#     def mergeNodes(self, head: Optional[Node]):
#         tmp = head
#         summa = 0
#         l= []
#         while tmp:
#             summa += tmp.data
#             if tmp.data == 0:
#                 l.append(summa)
#                 summa = 0
#             tmp = tmp.next
#         for _ in range(l.count(0)):
#             l.remove(0)
#         head = Node(l[0])
#         tmp = head
#         for i in l[1:]:
#             tmp.next = Node(i)
#             tmp = tmp.next
#         return head
#
#
# print(Solution().mergeNodes(head))
#

