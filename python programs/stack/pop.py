"""
Implement the pop method for the Stack class
that removes the top node from the stack and returns it.
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

    def pop(self):
        if self.top is None:
            return False
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        temp.next = None
        return True


my_stack = Stack(3)
my_stack.print()
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
print("my stack")
my_stack.print()
print("After popping")
my_stack.pop()
my_stack.print()