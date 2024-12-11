"""
Implement the prepend method
that inserts a new node with a given value at the beginning of the list.
"""

"""
Further extend the DoublyLinkedList class
by adding a pop method that removes the last node from the list and returns it.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True




my_double_linked_list = DoublyLinkedList(7)
my_double_linked_list.print_list()
print("============popping==============")
my_double_linked_list.print_list()