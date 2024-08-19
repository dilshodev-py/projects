"""stack
pop
empty
size
peek
push
"""

"""
queue (linked list)
stack (deque)

data structure
    list
    tuple
    set
    dict
    linked list
    tree
    graph
    namedTuple
    userDict
    userList
    
    
"""
class Node:
    def __init__(self , val= None , next = None):
        self.val = val
        self.next = next

class MyStack:
    def __init__(self):
        self.head = Node()
    def pop(self):
        tmp = self.head
        while tmp.next.next:
            tmp = tmp.next
        r_data = tmp.next.val
        tmp.next = None
        return r_data
    def push(self, data):
        new_node  = Node(data)
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node

    def peek(self):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp.val

    def empty(self):
        return not self.head.next
    def size(self):
        s = 0
        tmp = self.head.next
        while tmp:
            tmp = tmp.next
            s += 1
        return s
stack = MyStack()
stack.push(10)
stack.push(45)
stack.push(12)
stack.push(15)
print(stack.peek())
print(stack.empty())
print(stack.size())


