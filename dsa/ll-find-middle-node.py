# python program to find middle node in linked list without using length member

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_middle_node(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value

    def display(self):
        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)


my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
print("====this is the middle node====")
print(my_linked_list.find_middle_node())
print("====this is the linked list====")
my_linked_list.display()

