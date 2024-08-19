# Linkedlist
# Tree


# class Node:
#     def __init__(self, data = None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = Node()
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
#
# l = LinkedList()
# l.append(2)
# l.append(54)
# l.append(34)
# l.append(65)
# l.append(90)
# l.insert(4 , 100)
# l.remove(90)
# l.print()







# node1 = Node(1)
# node2 = Node(89)
# node3 = Node(34)
# node4 = Node(65)
# node5 = Node(12)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# l = [1, 89, 34, 65, 12]
# head = Node(l[0])
# tmp = head
# for i in l[1:]:
#     tmp.next = Node(i)
#     tmp= tmp.next






