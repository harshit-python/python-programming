"""
Implement the get method for the DoublyLinkedList class
that retrieves a node at a specific index in the list.
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

    def get(self, index):
        if index < 0 or index>= self.length:
            return None
        if index == 0:
            return self.head
        if index < self.length/2:
            temp = self.head
            count = 0
            while count != index:
                temp = temp.next
                count += 1
        else:
            count = self.length - 1
            temp = self.tail
            while count != index:
                temp = temp.prev
                count -= 1
        return temp


my_double_linked_list = DoublyLinkedList(7)
my_double_linked_list.append(6)
my_double_linked_list.print_list()
