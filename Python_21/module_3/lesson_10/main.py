
# list
# deque
# LifoQueue
# from collections import deque
# Stack + list         X
# Stack + deque
# Stack + Lifoqueue
# from queue import LifoQueue


# stack = LifoQueue()
# stack.put(10)
# stack.put(20)
# stack.put(30)
# a = stack.get()
# print(a)
# stack.put(a)
# print(stack.get())
# print(stack.qsize())
# print(stack.empty()) # O(1)
# from collections import deque

# list(range(1,1000000000))
# class Stack:
#     def __init__(self):
#         self.stack = deque()
#         self.size_stack = 0
#
#     def empty(self):
#         return not self.size_stack
#
#     def size(self):
#         return self.size_stack
#
#     def peek(self):
#         if not self.empty():
#             return self.stack[-1]
#         else:
#             print("Empty in stack!")
#
#
#     def push(self, data):
#         self.size_stack += 1
#         self.stack.append(data)
#
#     def pop(self):
#         if not self.empty():
#             self.size_stack -= 1
#             return self.stack.pop()
#         else:
#             print("Empty in stack!")
#
# #
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(10)
# print(s.empty())
# print(s.peek())
# print(s.size())
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
#
#
#
# l = [1,2,3,4,5]
#
# for i in l:  # O(N)
#     if i == 3:
#         print(i)
# l[2] # O(1)
#

# O(1)
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.pop()
# print(s.peek())
# print(s.empty())
# print(s.size())

# stack = deque()

# test = input(">>>")
# stack = deque()
# for i in test:
#     if ")" == i and stack and  stack[-1] == "(":
#         stack.pop()
#     elif "}" == i and stack and stack[-1] == "{":
#         stack.pop()
#     elif "]" == i and stack and stack[-1] == "[":
#         stack.pop()
#     else:
#         stack.append(i)
#
# print(not stack)
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue = deque()
#         self.size_ = 0
#
#     def empty(self):
#         return not self.size_
#
#     def push(self,data):
#         self.size_ += 1
#         self.queue.append(data)
#
#     def pop(self):
#         if not self.empty():
#             self.size_ -= 1
#             return self.queue.popleft()
#         else:
#             print("Empty in queue!")
#
#     def peek(self):
#         return self.queue[0]
#
#     def rear(self):
#         return self.queue[-1]

# q = Queue()
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# q.push(5)
# q.push(6)
# print(q.pop())
# print(q.pop())
# print(q.empty())
# print(q.rear())
# print(q.peek())

