"""
Implement the remove method for the DoublyLinkedList class
that removes a node at a specific index in the list and returns it.
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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        self.head = temp.next
        temp.next = None
        self.head.prev = None
        self.length -= 1
        return temp

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def print(self):
        temp = self.head
        while temp:
            if temp.next:
                print(temp.value, end=" -><- ")
            else:
                print(temp.value, end="")
            temp = temp.next
        print()

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

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp_node = self.get(index)
        if not temp_node:
            return None
        prev_node = temp_node.prev
        next_node = temp_node.next

        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

        temp_node.prev = None
        temp_node.next = None

        self.length -= 1
        return temp_node


my_double_linked_list = DoublyLinkedList(7)
my_double_linked_list.append(6)
my_double_linked_list.append(4)
my_double_linked_list.append(8)
my_double_linked_list.append(9)
my_double_linked_list.print()
print("--------after removing---------")
my_double_linked_list.remove(2)
my_double_linked_list.print()