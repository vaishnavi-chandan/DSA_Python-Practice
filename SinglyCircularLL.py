# Singly Circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and print nodes
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    # 3. Insert at a specific position (0-based)
    # def insert(self, new_node,pos):
    #          if pos==1: #Insert node at first
    #             temp = self.head
    #     if position == 0:
    #         new_node.next = self.head
    #         self.head = new_node
    #         return

    #     temp = self.head

    #     for _ in range(position - 1):
    #         if temp is None:
    #             print("Invalid position")
    #             return
    #         temp = temp.next

    #     if temp is None:
    #         print("Invalid position")
    #         return

    #     new_node.next = temp.next
    #     temp.next = new_node

    # 4. Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print(slow.data)
        else:
            print("Empty list")

    # 5. Delete node by value
    def delete(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        while temp and temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    # 6. Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous





ll = LinkedList()

    
values = [10, 20, 30, 40, 50]

for value in values:
    ll.append(value)

print("Linked List:")
ll.display()

print("Middle Node:")
ll.middle()

print("Insert 25 at position 2:")
ll.insert(25, 2)
ll.display()

print("Delete node 30:")
ll.delete(30)
ll.display()

print("Reversed List:")
ll.reverse()
ll.display()

print("Sum of consecutive nodes:")
ll.consecutive_sum()



    
