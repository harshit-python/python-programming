"""
Python program to implement linked list
"""
from select import select
from types import new_class


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def empty_list(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            return True
        temp = self.head
        new_node.next = temp
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp


    def set_value(self, index, value):
        if index<0 or index>=self.length:
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        temp_prev = self.get(index-1)
        temp_prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after









my_linked_list = LinkedList(4)
# my_linked_list.empty_list()
# my_linked_list.append(5)
# my_linked_list.append(3)
# my_linked_list.print_list()
# print("===========")
# my_linked_list.pop()
# my_linked_list.print_list()
# print("===========")
# my_linked_list.prepend(1)
# my_linked_list.print_list()
# print("===========")
# my_linked_list.empty_list()
# my_linked_list.prepend(2)
# my_linked_list.print_list()
# print("===========")
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.print_list()
print("===========")
my_linked_list.pop_first()
print("===========")
my_linked_list.print_list()
print("===========")
print("Value at index 1 is:", my_linked_list.get(1).value)
print("===========")
my_linked_list.print_list()
print("============")
my_linked_list.set_value(2, 6)
my_linked_list.print_list()
print("============")
my_linked_list.insert(1, 5)
my_linked_list.print_list()
print("============")
my_linked_list.remove(3)
my_linked_list.insert(1,2)
my_linked_list.insert(1,7)
my_linked_list.print_list()
print("============")
my_linked_list.reverse()
my_linked_list.print_list()
print("============")




