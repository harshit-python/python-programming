"""
Implement the insert method for the DoublyLinkedList class
that inserts a new node with a given value at a specific index in the list.
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

    # def print_list(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.value)
    #         temp = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            if temp.next:
                print(temp.value, end=" -><- ")
            else:
                print(temp.value, end="")
            temp = temp.next
        print()

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev_node = self.get(index-1)
        next_node = prev_node.next

        new_node.next = next_node
        new_node.prev = prev_node

        prev_node.next = new_node
        if next_node:
            next_node.prev = new_node
        self.length += 1
        return True



my_double_linked_list = DoublyLinkedList(7)
my_double_linked_list.append(6)
my_double_linked_list.append(4)
my_double_linked_list.append(8)
my_double_linked_list.append(9)
my_double_linked_list.print_list()
print("--------after inserting---------")
my_double_linked_list.insert(2, 3)
my_double_linked_list.print_list()

