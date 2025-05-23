"""
Create a Queue class
that represents a first-in, first-out (FIFO) data structure using a linked list implementation.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

my_queue = Queue(2)
my_queue.print()