"""
Implement the dequeue method for the Queue class
that removes the first node from the queue and returns it.
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

    def enqueue(self, value):
        if isinstance(value, list):
            for val in value:
                self.single_enqueue(val)
        else:
            self.single_enqueue(value)
        return True

    def single_enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return True
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
            self.length -= 1
            return temp
        self.first = temp.next
        temp.next = None
        self.length -= 1
        return temp

q = Queue(1)
q.enqueue(2)  # Enqueue a single value
q.enqueue([3, 4, 5])  # Enqueue multiple values
q.print()
q.dequeue()
print("after dequeue")
q.print()