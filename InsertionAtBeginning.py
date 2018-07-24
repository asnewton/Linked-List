"""Insertion at beginning of a circular Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def pushNode(self, item):
        new_node = Node(item)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def printList(self):
        curr = self.head
        if self.head is not None:
            while curr:
                print(curr.data)
                curr = curr.next
                if curr == self.head:
                    break


my_list = CircularLinkedList()
my_list.pushNode(1)
my_list.pushNode(3)
my_list.pushNode(6)
my_list.pushNode(7)
my_list.printList()

