
class Node:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    def __str__(self, level=0):
        string = '   ' * level + str(self.data) + '\n'
        for child in self.children:
            string += child.__str__(level+1)
        return string

branch1 = Node('SuperMario', [Node('Mario'),Node('Luigi'),Node('Princess Peach')])
branch2 = Node('MarioDo2', [Node('Shaggy'),Node('Velma'),Node('Scooby')])
branch1 = Node("MarioMovies", [branch1, branch2])
branch2 = Node('Minions', [Node('Gru'),Node('Kevin'),Node('Bob'),Node('Stuart')])
tree = Node("Movies", [branch1, branch2])

print(tree)

def print_leaves(node):
    if not node.children:
        print(node.data)
    for child in node.children:
        print_leaves(child)

print_leaves(tree)



