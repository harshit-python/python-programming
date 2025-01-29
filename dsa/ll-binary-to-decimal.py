# python program to convert binary number in linked list to decimal

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def binary_to_decimal(self):
        decimal_number = 0
        current = self.head

        # Traverse the linked list to calculate the decimal equivalent
        while current:
            decimal_number = decimal_number * 2 + current.value
            current = current.next

        return decimal_number

# Example Usage
ll = LinkedList()

# Binary number 1101 represented in the linked list
for bit in [1, 1, 0, 1]:
    ll.append(bit)

print("Binary Number in Linked List:")
ll.display()  # Output: 1 -> 1 -> 0 -> 1 -> None

decimal_number = ll.binary_to_decimal()
print("Decimal Equivalent:", decimal_number)  # Output: Decimal Equivalent: 13
