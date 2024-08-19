

class Node:
    def __init__(self , data = None , next = None):
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

l = LinkedList()
l.append(1)
l.append(89)
l.append(34)
l.append(65)
l.append(12)
l.insert(7 , 100)
l.print()





# n1 = Node(1)
# n2 = Node(89)
# n3 = Node(34)
# n4 = Node(65)
# n5 = Node(12)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# l = [1,89,34,65,12]
# head = Node(l[0])
# tmp = head
# for i in l[1:]:
#     tmp.next = Node(i)
#     tmp = tmp.next


# tmp: Node = head
# while tmp:
#     print(tmp.data)
#     tmp = tmp.next


# print()
# [1,89,34,65,12]

# tmp = n1
# while tmp:
#     print(tmp.data)
#     tmp = tmp.next


# l = [1,89,34,65,12]
# l.insert(3 , 100)
# print(l)

