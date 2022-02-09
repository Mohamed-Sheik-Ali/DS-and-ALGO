class Node:
    def __init__(self, data):
        self.data = data
        self.prevNode = None
        self.nextNode = None


class Doubly_Linked_List:

    def __init__(self):
        self.head = None

    def printDll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} ->", end="", sep="->")
                n = n.nextNode

    def printDll_reverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nextNode is not None:
                n = n.nextNode
            while n is not None:
                print(f"{n.data}", end="", sep="->")
                n = n.prevNode

    def Insert_when_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty")

    def Insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head.prevNode = new_node
            self.head = new_node

    def Insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nextNode is not None:
                n = n.nextNode
            n.nextNode = new_node
            new_node.prevNode = n


dll = Doubly_Linked_List()
dll.Insert_when_empty(20)
dll.Insert_at_beginning(10)
dll.Insert_at_end(100)
dll.printDll()
# dll.printDll_reverse()
