# python program to remove duplicates from linked list
from select import select


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

def remove_duplicates(ll):
    if not ll.head.next:
        return None
    current = ll.head
    prev = None
    seen = set()
    while current:
        if current.value in seen:
            prev.next = current.next
        else:
            seen.add(current.value)
            prev = current
        current = current.next


ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)


print("Original List:")
ll.print_list()  # Output: 1 -> 2 -> 3 -> 2 -> 4 -> 3 -> 5 -> None

remove_duplicates(ll)
print("List After Removing Duplicates:")
ll.print_list()