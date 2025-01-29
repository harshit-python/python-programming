"""
Extend the previously implemented DoublyLinkedList class
by adding an append method that inserts a new node with a given value at the end of the list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        while self.head:
            print(self.head.value)
            self.head = self.head.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

my_double_linked_list = DoublyLinkedList(7)
my_double_linked_list.append(6)
my_double_linked_list.print_list()
