"""Mavzu
stack - chiziqli malumot saqlash
queue - chiziqli malumot saqlash
Linked list
"""
# stack - array , collections.deque (FILO or LIFO)
# queue - array , queue.Queue (FIFO or LILO)
# Linked - Node

# =================== array ===================
# import time

# # stack = []
# # start = time.time()
# # for i in range(1000000):
# #     stack.append(i)
# #
# # for i in range(1000000):
# #     print(stack.pop())
# # print(time.time() - start)
# # =================== deque ===================
# from collections import deque

# #
# stack = deque()
# stack.append(1)
#
# start = time.time()
# for i in range(1000000):
#     stack.append(i)

# for i in range(1000000):
#     print(stack.pop())
# print(time.time() - start)


# "(()()()"
# stack = ["("]
# from collections import deque
#
#
# class Stack:
#     def __init__(self):
#         self.stack = deque()
#         self.stack_size = 0
#
#     def empty(self) -> bool:
#         return self.stack_size == 0
#
#     def size(self) -> int:
#         return self.stack_size

#     def peek(self):
#         return self.stack[-1]
#
#     def pop(self):
#         if not self.empty():
#             self.stack_size -= 1
#             return self.stack.pop()
#         else:
#             return "Stack empty!"
#
#     def push(self, data):
#         self.stack_size += 1
#         self.stack.append(data)
#
# s = Stack()
# s.push(1)
# s.push(2)
# s.push("hello")
# s.pop()
# print(s.stack_size)
# print(s.peek())
# print(s.empty())

# ===================== queue ===========================


# queue = []
#
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
# from builtins import Exception
# from queue import Queue

# queue = Queue(maxsize=3)
#
# queue.put(1)
# queue.put(2)
# queue.put(3)
# print(queue.get_nowait()) # O(1)
# print(queue.get_nowait())
# print(queue.get_nowait())

# class Queue:
#     def __init__(self, maxsize = None):
#         self.queue = []
#         self.maxsize = maxsize
#         self.q_size = 0
#
#     def empty(self):
#         return not self.q_size
#
#     def size(self):
#         return self.q_size
#
#     def bottom(self):
#         return self.queue[0] if self.queue else None
#
#
#     def put(self, data):
#         if self.q_size < self.maxsize:
#             self.q_size += 1
#             self.queue.append(data)
#
#     def full(self):
#         return self.q_size == self.maxsize
#     def get(self):
#         if not self.empty():
#             self.q_size -= 1
#             return self.queue.pop(0)
#
# q = Queue(maxsize=3)
#
# for i in range(10):
#     if not q.full():
#         q.put(i)
#     else:
#         break
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# Linked list


class Node:
    def __init__(self, data = None , next = None):
        self.data = data
        self.next = next

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# head = n1
# while n1:
#     print(n1.data)
#     n1 = n1.next
# print(n1)
# head = n1
# while n1:
#     print(n1.data)
#     n1 = n1.next

# numbers = range(1, 100)
# head = Node(numbers[0])
# tmp = head
# for i in numbers[1:]:
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# tmp = head
# while tmp:
#     print(tmp.data)
#     tmp = tmp.next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node


    def pop(self):
        tmp = self.head
        while tmp.next and tmp.next.next:
            tmp = tmp.next
        tmp.next = None

    def size(self):
        tmp = self.head.next
        c = 0
        while tmp:
            c += 1
            tmp = tmp.next
        return c

    def insert(self, data , place):
        new_node = Node(data)
        tmp = self.head
        space = 0
        while tmp.next:
            space += 1
            if space == place:
                new_node.next = tmp.next
                tmp.next = new_node
                break
            tmp = tmp.next
        else:
            tmp.next = new_node





    def show(self):
        tmp = self.head.next
        while tmp:
            print(tmp.data, end = " ")
            tmp = tmp.next
        print()

    def popleft(self):
        tmp = self.head # None
        tmp.next = tmp.next.next # 6





l = LinkedList()
l.append(1)
l.append(2)
l.append(6)
l.show()
l.insert(10 , 100)
l.show()
























