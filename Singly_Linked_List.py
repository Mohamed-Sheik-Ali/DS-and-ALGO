# Create a Node.
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

# List which contains all the nodes.


class LinkedList():

    def __init__(self):
        self.head = None

    # Traversing through Linked List
    def printL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} ->", end="")
                n = n.next_node

    # To add or insert a node in the beginning
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # To add or insert a node in the end
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next_node is not None:
                n = n.next_node
            n.next_node = new_node

    # To add a node in-between after a given node(x)
    def add_after_given_node(self, data, x):
        n = self.head

        while n is not None:
            if x == n.data:
                break
            n = n.next_node
        if n is None:
            print("Node doesn\'t exist")
        else:
            new_node = Node(data)
            new_node.next_node = n.next_node
            n.next_node = new_node

    # To add a node in-between before a given node(x)
    def add_before_given_node(self, data, x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
            return

        n = self.head

        while n.next_node is not None:
            if n.next_node.data == x:
                break
            n = n.next_node

        if n.next_node is None:
            print("Node doesn\'t exist")
        else:
            new_node = Node(data)
            new_node.next_node = n.next_node
            n.next_node = new_node


Ll = LinkedList()
Ll.add_at_beginning(10)
Ll.add_at_end(21)  # will add at the end of the linked list
Ll.add_at_beginning(50)
Ll.add_before_given_node(11, 21)
Ll.add_after_given_node(100, 10)
Ll.add_after_given_node(200, 100)
Ll.printL()
