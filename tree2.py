
class Node:

    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        string = '   ' * level + str(self.data) + '\n'
        for child in self.children:
            string += child.__str__(level+1)
        return string


tree = Node('root', [Node('a', [Node(1),Node(2,[Node('Mario'),Node('Luigi'),Node('Princess Peach')])]),Node('b'),Node('c')])

print(tree)
