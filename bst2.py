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
    def traversal(self):
        return _traverse(self.root, [])
    def height(self):
        return _height(self.root)

def _traverse(node, lst):
    """in-order traversal"""
    if node.left:
        _traverse(node.left, lst)
    lst.append(node.data)
    if node.right:
        _traverse(node.right, lst)
    return lst

def _height(node):
    if not node:
        return -1
    leftheight = _height(node.left)
    rightheight = _height(node.right)
    return 1 + max(leftheight, rightheight)

class BST(Tree):
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


bst = BST()
from random import randint
for _ in range(36):
    bst.insert(randint(1,5) * randint(1,3))
print(bst)
#print(bst.traversal())
print("height:", bst.height())
