from collections import deque

# ctrl + alt + m

class Stack:
    def __init__(self):
        self.stakan = deque()
        self.size = 0

    def push(self, data):
        self.stakan.append(data)
        self.size += 1

    def pop(self):
        if self.empty():
            return "Stack is empty"
        self.size -= 1
        return self.stakan.pop()

    def empty(self):
        return not self.size

    def top(self):
        if self.empty():
            return "Stack is empty"
        return self.stakan[-1]

    def size_stack(self):
        return self.size


def is_balanced(string):
    stack = Stack()
    tmp = {")": "(", "}": "{", "]": "["}
    for i in string:
        if i in tmp.keys() and stack.top() == tmp[i]:
            stack.pop()
        else:
            stack.push(i)
    return stack.empty()


test = '(((((())))'
print(is_balanced(test))  # True


# ============================================================


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, pos, data):
        tmp = self.head.next
        position = 1
        new_node = Node(data)
        while tmp.next:
            position += 1
            if pos == position:
                new_node.next = tmp.next
                tmp.next = new_node
                break
            tmp = tmp.next
        else:
            tmp.next = new_node

    def append(self, data):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data)

    def print(self):
        tmp = self.head.next
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def delete(self, value):
        tmp = self.head
        while tmp.next:
            if tmp.next.data == value:
                tmp.next = tmp.next.next
                break

            tmp = tmp.next

    def find(self, value):
        tmp = self.head
        pos = 0
        while tmp.next:
            pos += 1
            if tmp.next.data == value:
                return pos
            tmp = tmp.next

    def duplicate_delete(self):
        tmp = self.head.next
        while tmp:
            tmp2 = tmp.next
            while (not tmp2 is None) and tmp2.data == tmp.data:
                tmp2 = tmp2.next
            tmp.next = tmp2
            tmp = tmp.next


# 16:10
# Telegram Bot -> instagram download

l = LinkedList()
l.append(1)
l.append(4)
l.append(4)
l.append(7)
l.append(8)

l.duplicate_delete()
l.print()
