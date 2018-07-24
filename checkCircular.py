"""Check if a linked list is Circular Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertSorted(self, item):
        new_node = Node(item)
        temp = self.head
        # if list is empty
        if self.head is None:
            new_node.next = new_node
            self.head = new_node

        # insert at end/beginning
        elif temp.data >= new_node.data:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

        # sorted insert at any position
        else:
            while temp.next != self.head and temp.next.data < new_node.data:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node


    def printList(self):
        temp = self.head
        if self.head is not None:
            while temp:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    print("Linked List is Circular")
                    break

my_list = CircularLinkedList()
my_list.insertSorted(7)
my_list.insertSorted(1)
my_list.insertSorted(6)
my_list.insertSorted(3)
my_list.printList()
