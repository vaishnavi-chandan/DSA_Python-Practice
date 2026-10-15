
class Node:
    def __init__(self, val):
        self.prev = None
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    def insert(self, new_node, pos):
        temp = self.head

        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node

        else:
            p = 1
            while p != pos - 1 and temp.next:
                temp = temp.next
                p += 1

            new_node.next = temp.next
            new_node.prev = temp

            if temp.next:
                temp.next.prev = new_node

            temp.next = new_node


    def print(self):
        temp = self.head
        print("List elements:", end=" ")
        while temp.next:
            # print(temp.data, end=" ")
            temp = temp.next
        while(temp):
            print(temp.data, end=" ")
            temp = temp.prev
        print()


list = LinkedList()
list.append(Node(12))
list.append(Node(102))
list.append(Node(52))
list.append(Node(56))

list.print()

list.insert(Node(5), 1)
list.print()

# Write a function print node values in reverse order in doubly linear linked list.
