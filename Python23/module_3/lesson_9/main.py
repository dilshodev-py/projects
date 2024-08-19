# list    - python built-in
# deque() - collection
# from collections import deque
# from queue import Queue
# q = Queue(maxsize=1)

















class Stack:
    def __init__(self):
        self.stakan = deque()
        self.size = 0

    def push(self, data):
        self.stakan.append(data)
        self.size += 1

    def pop(self):
        if self.empty():
            return "Stakan bo'sh"
        self.size -= 1
        return self.stakan.pop()

    def empty(self):
        return not self.size

    def top(self):
        if self.empty():
            return "Stakan bo'sh"
        return self.stakan[-1]

    def size_stack(self):
        return self.size


# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.top())
# print(s.size_stack())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.size_stack())

# def reverse_string(string) -> str:
#     s = Stack()
#     for i in string:
#         s.push(i)
#     result = ""
#     while not s.empty():
#         result += s.pop()
#     return result


# print(reverse_string("hello"))

# 2 min : 16:40



