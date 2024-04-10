
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


tree = Node('root',
           Node('a',
               Node(1),
               Node(2,
                   Node('Mario'),
                   Node('Luigi'))),
           Node('b'))


print(tree)

def traverse(node):
    "in-order traversal"
    if node.left:
        traverse(node.left)
    print(node.data, end=' ')
    if node.right:
        traverse(node.right)

print("\nin order traversal:")
traverse(tree)
print()

def height(node):
    if not node:
        return -1
    return 1 + max(height(node.left), height(node.right))

print("\nthe height is:", height(tree))
