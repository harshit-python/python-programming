"""
Implement the set_value method for the DoublyLinkedList class
that updates the value of a node at a specific index in the list.
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
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

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

    def set(self, index, value):
        desired_node = self.get(index=index)
        if desired_node is None:
            return False
        else:
            desired_node.value = value
            return True


my_double_linked_list = DoublyLinkedList(7)
my_double_linked_list.append(6)
my_double_linked_list.append(8)
my_double_linked_list.append(9)
my_double_linked_list.print_list()
print("=================")
my_double_linked_list.set(1, 8)
my_double_linked_list.print_list()
