from math import log2


# BinaryTree Search BIG(log2(n))


# BinaryTree Sort BIG(log2(n))


# BinaryTree Memory


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insertTree(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insertTree(data)
            else:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insertTree(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data, end=' ')
        if self.right:
            self.right.printTree()

    def maxDepth(self):
        if not self:
            return 0
        ldepth = 0
        rdepth = 0
        if self.left:
            ldepth = self.left.maxDepth()
        if self.right:
            rdepth = self.right.maxDepth()
        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

    def search(self, data):
        if self is None or self.data == data:
            return self
        if self.data < data:
            if self.right:
                return self.right.search(data)
        if self.left:
            return self.left.search(data)

    # def index(self,data , level):
    #     if self.data == data:
    #         return level
    #     level += 1
    #     if self.left:
    #         if self.left.data == data:
    #             return f"level {level} , left"
    #         else:
    #             return self.left.search(data , level)
    #     if self.right:
    #         if self.right.data == data:
    #             return f"level {level} , right"
    #         else:
    #             return self.right.search(data , level)
    #     return f"level {level}"
    def getLevelUtil(self, data, level):
        if (self == None):
            return 0

        if (self.data == data):
            return level
        downlevel = 0
        if self.left:
            downlevel = self.left.getLevelUtil(data, level + 1)
        if (downlevel != 0):
            return downlevel
        if self.right:
            downlevel = self.right.getLevelUtil(data, level + 1)
        return downlevel

    def getLevel(self, data):
        return self.getLevelUtil(data, 0)

    def __str__(self):
        return f"{self.data}"

# l = [90, 65, 12, 87, 34, 16]

# root = TreeNode(90)
# n1 = TreeNode(65)
# n2 = TreeNode(12)
# n3 = TreeNode(87)
# n4 = TreeNode(34)
# n5 = TreeNode(16)
#
# root.left = n1
# n1.left = n2
# n1.right = n3
# n2.right = n4
# n4.left = n5

# root = TreeNode(65)
# n1 = TreeNode(34)
# n2 = TreeNode(12)
# n3 = TreeNode(78)
# n4 = TreeNode(45)
#
#
# root.left = n1
# n1.left = n2
# root.right = n3
# n1.right = n4
