
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LList:
    def __init__(self):
        self.head = None

    def prepend(self, val):
        pass

    def append(self, val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = newnode

    def remove(self, val):
        pass

    def insert_after(self, current, val):
        pass

    def __str__(self):
        """Return a string representation."""

        string = ""
        if self.head is None:
            return string
        node = self.head
        while node.next:
            string += str(node.val) + ", "
            node = node.next
        string += str(node.val)
        return string
