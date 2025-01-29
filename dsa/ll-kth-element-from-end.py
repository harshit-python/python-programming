# python program to find kth element from end in a linked list

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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

def kth_element_from_end(my_linked_list, k):
    if not my_linked_list.head:
        return None
    slow = my_linked_list.head
    fast = my_linked_list.head
    for i in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = kth_element_from_end(my_linked_list, k)

print(result.value)  # Output: 4
