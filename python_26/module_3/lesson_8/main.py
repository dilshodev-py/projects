class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self , item):
        if self.value:
            if self.value > item:
                if self.left is None:
                    self.left = BinaryTree(item)
                else:
                    self.left.insert(item)
            else:
                if self.right is None:
                    self.right = BinaryTree(item)
                else:
                    self.right.insert(item)
        else:
            self.value = item

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()












l = [8, 5, 10, 45, 1, 3, 2, 5]
root = BinaryTree()
for i in l:
    root.insert(i)

root.print_tree()



# n1 = BinaryTree(8)
# n2 = BinaryTree(5)
# n3 = BinaryTree(10)
# n4 = BinaryTree(45)
# n5 = BinaryTree(1)
# n6 = BinaryTree(3)
# n7 = BinaryTree(2)
# n8 = BinaryTree(5)
#
# n1.left = n2
# n1.right = n3
# n2.left = n5
# n2.right = n8
# n3.right = n4
# n5.right = n6
# n6.left = n7



