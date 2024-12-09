# python program to sort linked list into 2 partitions

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def partition_list(self, val):
        less_than_val = LinkedList()
        more_than_val = LinkedList()
        temp = self.head
        while temp.next:
            if temp.value < val:
                less_than_val.append(temp.value)
            else:
                more_than_val.append(temp.value)
            temp = temp.next
        tail = less_than_val.head
        while tail.next:
            tail = tail.next
        tail.next = more_than_val.head
        return less_than_val


# function to convert linked list to list
def linkedlist_to_list(head):
    result_list = []
    while head:
        result_list.append(head.value)
        head = head.next
    return result_list


ll = LinkedList()
for i in [3, 5, 8, 5, 10, 2, 1]:
    ll.append(i)

print("Original List:")
ll.print_list()

partitioned_list = ll.partition_list(5)
print("Partitioned List (Pivot=5):")
partitioned_list.print_list()