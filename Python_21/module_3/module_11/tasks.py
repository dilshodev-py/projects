# # task - delete(LinkedList)
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = Node()
#
#     def delete(self, data):
#         tmp = self.head
#         while tmp.next:
#             if tmp.next.data == data:
#                 tmp.next = tmp.next.next
#                 break
#             tmp = tmp.next
#
#
#     def append(self, data):
#         new_node = Node(data)
#         tmp = self.head
#         while tmp.next:
#             tmp = tmp.next
#         tmp.next = new_node
#
#     def print(self):
#         tmp = self.head.next
#         while tmp:
#             print(tmp.data, end = " ")
#             tmp = tmp.next
#
#     def empty(self):
#         return not self.head.next
#
#     def pop(self):
#         tmp = self.head
#         if self.empty():
#             print("Empty in linked list !")
#             return
#         while tmp.next.next:
#             tmp = tmp.next
#         tmp.next = None
#
#     def insert(self, pos, data):
#         new_node = Node(data)
#         tmp = self.head
#         count_pos = 0
#         while tmp.next:
#             count_pos += 1
#             if count_pos == pos:
#                 new_node.next = tmp.next
#                 tmp.next = new_node
#                 break
#             tmp = tmp.next
#         else:
#             tmp.next = new_node
#
#     def clear(self):
#         self.head.next = None
#
# l = LinkedList()
# l.append(2)
# l.append(54)
# l.append(34)
# l.append(65)
# l.append(90)
# l.print()
# l.delete(2)
# print()
# l.print()

# l = set([1,2])
# l.remove(2)
# print(l)