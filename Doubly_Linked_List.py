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
                print(f"{n.data} ->", end="")
                n = n.nextNode

    def printDll_reverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nextNode is not None:
                n = n.nextNode
            while n is not None:
                print(f"{n.data} -> ", end="")
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

    def add_after_given_node(self, data, x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nextNode
            if n is None:
                print("Node doesn't exist")
            else:
                new_node = Node(data)
                new_node.nextNode = n.nextNode
                new_node.prevNode = n
                if n.nextNode is not None:
                    n.nextNode.prevNode = new_node
                n.nextNode = new_node

    def add_before_given_node(self, data, x):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nextNode
            if n is None:
                print("Node doesn't exist")
            else:
                new_node = Node(data)
                new_node.nextNode = n
                new_node.prevNode = n.prevNode
                if n.prevNode is not None:
                    n.prevNode.nextNode = new_node
                else:
                    self.head = new_node
                n.prevNode = new_node


dll = Doubly_Linked_List()
dll.Insert_when_empty(20)
dll.Insert_at_beginning(10)
dll.Insert_at_end(100)
dll.add_after_given_node(11, 100)
dll.add_before_given_node(12, 100)
dll.printDll()
# dll.printDll_reverse()
