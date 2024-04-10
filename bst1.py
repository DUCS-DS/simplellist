class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self, level=0):
        string = '   ' * level + str(self.data) + '\n'
        for child in [self.left, self.right]:
            if child:
                string += child.__str__(level+1)
        return string

class Tree:
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.root)
    def insert(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            node = self.root
            while node:
                if item < node.data:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(item)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(item)
                        break
    def traversal(self):
        traverse(self.root)

def traverse(node):
    """in-order traversal"""
    if node.left:
        traverse(node.left)
    print(node.data, end= ' ')
    if node.right:
        traverse(node.right)

def height(node):
    if not node:
        return -1
    leftheight = height(node.left)
    rightheight = height(node.right)
    return 1 + max(leftheight, rightheight)


bst = Tree()
from random import randint
for _ in range(16):
    bst.insert(randint(1, 20))
print(bst)
print("in order traversal:")
bst.traversal()
print()
print("height:", height(bst.root))
