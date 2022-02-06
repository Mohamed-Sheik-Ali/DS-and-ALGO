# 1) Create a Node.

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

# 2) List which contains all the nodes.
class LinkedList():

    def __init__(self):
        self.head = None

    def printL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

Ll = LinkedList()
Ll.printL()