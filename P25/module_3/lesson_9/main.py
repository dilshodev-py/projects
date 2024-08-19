''''''
import time
from collections import deque, namedtuple
from queue import Queue

"""
collections
    list
    set
    dict
    str
    Enum
    deque
    queue
    userDict
    userList
    Counter
    
data structure
    Stack
    Queue
    LinkedList
    Tree
    Graph
"""

# from queue import Queue

# q = Queue(4)
# q.put(10)
# q.put(20)
# q.put(30)
# print(q.full())
# print(q.queue)

# s = "tweriwurh"
# print(Counter(s))

"""
t : 1
w : 2
...
"""

# d = UserDict({"name" : "Botir" , "age" : 23})
# d = OrderedDict({"name" : "Botir" , "age" : 23})
# print(d)
# d.move_to_end('name')
# print(d)

# l = UserList([1,2,3,4,5,6,7])

# s = UserString("sfdsgwgre")

# l = [1,2,3,4,5,6,7]
# d = deque([1,2,3,4,5,6,7])
# print(d.appendleft(0))
# print(d.remove(3))


"""
data structure
    Stack
    Queue
    LinkedList
    Tree
    Graph
"""

#
# class Stack:
#     def __init__(self):
#         self.data = deque()
#         self.len = 0
#
#     def empty(self):
#         return not self.data
#
#     def size(self):
#         return self.len
#
#     def top(self):
#         if self.size() == 0:
#             return "Empty Stack"
#         return self.data[-1]
#
#     def push(self, x):
#         self.data.append(x)
#         self.len += 1
#
#     def pop(self):
#         if self.size() == 0:
#             return "Empty Stack"
#         self.len -= 1
#         return self.data.pop()
#
#     def peek(self):
#         return self.top()


# maxsize
# empty()
# full()
# get()
# get_nowait()
# put(item)
# put_nowait(item)
# qsize()

# class MyQueue:
#     def __init__(self, maxsize=0):
#         self.maxsize = maxsize
#         self.data = deque()
#         self.len = 0
#
#     def empty(self):
#         return not self.len
#
#     def full(self):
#         return self.maxsize == self.len
#
#     def get(self):
#         while not self.data:
#             time.sleep(1)
#         self.len -= 1
#         return self.data.popleft()
#
#     def get_nowait(self):
#         if not self.data:
#             raise Exception("Queue is empty")
#         self.len -= 1
#         return self.data.popleft()
#
#     def put(self, x):
#         while self.full():
#             time.sleep(1)
#         self.data.append(x)
#         self.len += 1
#
#     def put_nowait(self, x):
#         if self.full():
#             raise Exception("Queue is full")
#         self.data.append(x)
#         self.len += 1
#
#     def qsize(self):
#         return self.len
#
#     def __repr__(self):
#         return str(self.data)
#

# q = MyQueue(maxsize=3)
# q.put(10)
# q.put(20)
# q.put(30)
# q.get()
# print(q)

"{[}]()"
# False
# data = "(())"
# s = Stack()
# check = {")": "(", "}": "{", "]": "["}
# for i in data:
#     if i in check.keys() and not s.empty() and check.get(i) == s.top():
#         s.pop()
#     else:
#         s.push(i)
# print(s.empty())

# Time - > 16:10
# s = Stack()
# s.push(20)
# s.push(5)
# print(s.top())
# print(s.size())
# print(s.pop())
# print(s.pop())
# print(s.size())
# print(s.empty())


from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


# print(Season(2).name)
# print(type(Season.SPRING))
# print(list(Season))


# class Role(Enum):
#     ADMIN = 1
#     SALES = 2
#     RECEPTION = 3

# menu = """
#     1) Admin
#     2) Sales
#     3) Reception
#     >>>"""
# key = int(input(menu))
# print(Role(key).name)
# if key == 1:
#     print('ADMIN')
# elif key == 2:
#     print('SALES')
# elif key == 3:
#     print('RECEPTION')



# ==========================================


# d = {
#     "name" : "Botir",
#     "age" : 25,
#     "birthday" : "1999-01-01"
# }
# class UserDTO:
#     def __init__(self, name, age, birthday):
#         self.name = name
#         self.age = age
#         self.birthday = birthday

# User = namedtuple('User' , list(d.keys()))
#
# print(User(**d).birthday)


# LinkedList
# Tree








