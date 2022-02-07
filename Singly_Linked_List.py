# 1) Create a Node.
class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

# 2) List which contains all the nodes.


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
    # 3) To add or insert a node in the beginning
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next_node is not None:
                n = n.next_node
            n.next_node = new_node

    def add_in_between(self, data):
        new_node = Node(data)


Ll = LinkedList()
Ll.add_at_beginning(10)
Ll.add_at_end(21) # will add at the end of the linked list
Ll.add_at_beginning(50)
Ll.printL()
