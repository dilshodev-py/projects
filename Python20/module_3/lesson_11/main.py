"""
LinkedList
    head node
    Nodes
    data
    next

stack -> array , collection.deque
queue -> array , queue.Queue

Tree
    root node
    Nodes
    data
    left
    right
"""
#
# class Node:
#     def __init__(self, val= None , next = None):
#         self.val = val
#         self.next = next
#
#
# class MyLinkedList:
#     def __init__(self):
#         self.head = Node()
#
#     def get(self, index: int) -> int:
#         tmp = self.head.next
#         i = 0
#         while tmp:
#             if i == index:
#                 return tmp.val
#             i += 1
#             tmp = tmp.next
#         else:
#             return -1
#
#     def addAtHead(self, val: int) -> None:
#         new_node = Node(val)
#         new_node.next = self.head.next
#         self.head.next = new_node
#
#
#
#     def addAtTail(self, val: int) -> None:
#         tmp = self.head
#         new_node = Node(val)
#         while tmp.next:
#             tmp = tmp.next
#         tmp.next = new_node
#
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         tmp = self.head
#         new_node = Node(val)
#         i = -1
#         while tmp.next:
#             if i + 1 == index:
#                 new_node.next = tmp.next
#                 tmp.next = new_node
#                 break
#             i += 1
#             tmp = tmp.next
#         else:
#             if i+1 == index:
#                 tmp.next = new_node
#
#
#
#
#
#     def deleteAtIndex(self, index: int) -> None:
#         tmp = self.head
#         i = -1
#         while tmp and tmp.next:
#             if i + 1 == index:
#                 tmp.next = tmp.next.next
#             i += 1
#             tmp = tmp.next



#
# head = MyLinkedList()
# head.addAtHead(10)
# head.addAtHead(12)
# head.addAtTail(13)
# head.addAtIndex(1, 20)
# head.deleteAtIndex(1)
# print(head.get(1))

# 12 10 13

# python basic -> list , int , tuple
# python OOP -> tamoillar
# Thread
# Process
# async
# algorithm
# database
# Docker , redis , git , github , Docker Hub , Tg Bot
# Framework -> DJANGO (jinja , restapi) , FASTAPI

