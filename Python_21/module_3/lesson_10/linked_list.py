class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = new_node

    def print(self):
        tmp = self.head.next
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def empty(self):
        return not self.head.next

    def pop(self):
        tmp = self.head
        if self.empty():
            print("Empty in linked list !")
            return
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None

    def insert(self, pos, data):
        new_node = Node(data)
        tmp = self.head
        count_pos = 0
        while tmp.next:
            count_pos += 1
            if count_pos == pos:
                new_node.next = tmp.next
                tmp.next = new_node
                break
            tmp = tmp.next
        else:
            tmp.next = new_node

    def clear(self):
        self.head.next = None


# Leetcode -> min : 5
# Leetcode -> stack : 3
# Leetcode -> queue : 2
# Canva    -> tasks
# video    -> main task


l = LinkedList()
l.append(10)
l.append(20)
l.insert(3, 0)
l.clear()
l.print()

#
# l = list(range(1, 100))
# head = Node(l[0])
# tmp = head
# for i in l[1:]:
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# tmp = head
# while tmp:
#     print(tmp.data)
#     tmp = tmp.next


# node1 = Node(1)
# node2 = Node(89)
# node3 = Node(34)
# node4 = Node(65)
# node5 = Node(12)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5


# tmp = node1
# while tmp:
#     print(tmp.data)
#     tmp = tmp.next


d = [
    {
        "id": 1,
        "name": "Ikki dunyo",
        "image": "https://telegra.ph/file/a7d72d0c776605249fe51.png",
        "price": 150000,
    },
    {
        "id": 2,
        "name": "Oq kema",
        "image": "https://telegra.ph/file/d438ec818cb3dcd460243.png",
        "price": 100000,
    },
{
        "id": 3,
        "name": "Pycharm Book",
        "image": "https://telegra.ph/file/feab6d06b25dc6231e686.png",
        "price": 1000000,
    },
{
        "id": 4,
        "name": "Docker",
        "image": "https://telegra.ph/file/48a817e55b67756572ed0.png",
        "price": 1200000,
    }
]
