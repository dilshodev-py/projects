res = []


class NodeTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if self.data <= data:
                if self.right is None:
                    self.right = NodeTree(data)
                else:
                    self.right.insert(data)
            else:
                if self.left is None:
                    self.left = NodeTree(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inorder_list(self):
        if self.left:
            self.left.inorder_list()
        res.append(self.data)
        if self.right:
            self.right.inorder_list()


l = [10, 5, 15, 3, 7, 13, 18, 1, 6]
root = NodeTree(l[0])
for i in l[1:]:
    root.insert(i)
root.inorder_list()
print(res)






