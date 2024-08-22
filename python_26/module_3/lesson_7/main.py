# import time
# from collections import deque
#
# data = deque()
#
#
# class Stack:
#     data = deque()
#     lensize = 0
#
#     def empty(self):
#         return not self.lensize
#
#     def push(self , d):
#         self.data.append(d)
#         self.lensize += 1
#     def pop(self):
#         if self.empty():
#             return "Stack is empty"
#         self.lensize -= 1
#         return self.data.pop()
#     def peek(self):
#         if self.empty():
#             return "Stack is empty"
#         return self.data[-1]
#
#     def size(self):
#         return self.lensize
#
#
#
# class Queue:
#     def __init__(self, maxsize = None):
#         self.maxsize = maxsize
#     data = deque()
#     lensize = 0
#
#     def empty(self):
#         return not self.lensize
#
#     def full(self):
#         return self.maxsize == self.lensize
#     def get(self):
#         while self.empty():
#             time.sleep(0.5)
#
#         self.lensize -= 1
#         return self.data.popleft()
#
#     def get_nowait(self):
#         assert not self.empty(), "Queue is empty"
#         self.lensize -= 1
#         return self.data.popleft()
#
#     def put(self , item):
#         while self.full():
#             time.sleep(0.5)
#         self.lensize += 1
#         self.data.append(item)
#
#     def put_nowait(self , item):
#         assert not self.full() , 'Queue is full'
#         self.lensize += 1
#         self.data.append(item)
#
#     def qsize(self):
#         return self.lensize


# ===========================================


class Node:
    def __init__(self, data= None , next = None):
        self.data = data
        self.next = next



class LinkedList:
    head = Node()
    last = head
    def append(self , item):
        new_node = Node(item)
        self.last.next = new_node
        self.last = new_node

    def appendleft(self, item):
        pass


    def insert(self, item, position):
        tmp = self.head
        pos = 1
        while tmp.next:
            if pos == position:
                new_node = Node(item)
                new_node.next = tmp.next
                tmp.next = new_node
                return
            pos += 1
            tmp = tmp.next
        tmp.next = Node(item)

    def print(self):
        tmp = self.head.next
        while tmp:
            print(tmp.data)
            tmp = tmp.next

l = LinkedList()

l.append(1)
l.append(2)
l.append(3)
l.insert(10 , 2)

l.print()




# n1 = Node("a")
# n2 = Node(2.0)
# n3 = Node({"1" : 1})
# n4 = Node([1,2,3])
# n5 = Node((1,2,3))
# n6 = Node({1,2,3})
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
#
# tmp = n1
# while tmp:
#     print(tmp.data)
#     tmp = tmp.next

