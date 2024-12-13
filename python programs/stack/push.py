"""
Implement the push method for the Stack class
that adds a new node with a given value to the top of the stack.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.height += 1
            return True
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True


my_stack = Stack(3)
print("-----Initialising Stack-----")
my_stack.print()
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
print("After pushing")
my_stack.print()