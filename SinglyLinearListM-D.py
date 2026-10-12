
class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.Next:
                temp = temp.Next
            temp.Next = new_node

    # Find middle node and delete it
    def delete_middle_node(self):
        temp = temp1 = self.head
        prev = None

        while temp1 and temp1.Next:
            prev = temp
            temp = temp.Next
            temp1 = temp1.Next.Next

        if temp:
            print("Deleting middle node:", temp.data)
            if prev:
                prev.Next = temp.Next
            else:
                self.head = None

    # Delete first node
    def delete_first(self):
        temp = self.head

        if temp:
            print("Deleted first node:", temp.data)
            self.head = temp.Next
        else:
            print("List is empty")

    # Delete last node
    def delete_last(self):
        temp = self.head

        if temp is None:
            print("List is empty")
        elif temp.Next is None:
            print("Deleted last node:", temp.data)
            self.head = None
        else:
            while temp.Next.Next:
                temp = temp.Next

            print("Deleted last node:", temp.Next.data)
            temp.Next = None

    # Delete alternate nodes
    def delete_alternate(self):
        temp = self.head

        while temp and temp.Next:
            temp.Next = temp.Next.Next
            temp = temp.Next

    # Concatenate two linked lists
    def concatenate(self, head2):
        temp = self.head

        if temp is None:
            self.head = head2
            return

        while temp.Next:
            temp = temp.Next

        temp.Next = head2

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.Next

        print()


# Main program
ll = LinkedList()
list2 = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

list2.append(60)
list2.append(70)
list2.append(80)

print("Original list:")
ll.display()

ll.delete_middle_node()
ll.display()

ll.delete_first()
ll.display()

ll.delete_last()
ll.display()

ll.delete_alternate()
ll.display()

ll.concatenate(list2.head)
print("After concatenation:")
ll.display()
