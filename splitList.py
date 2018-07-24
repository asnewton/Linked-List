"""Split a Circular Linked List into two halves"""

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

    def split(self, listA, listB):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is None:
            return
        while fast_ptr.next != self.head or fast_ptr.next.next != self.head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next

        listA.head = self.head

        if self.head.next != self.head:
            listB.head = slow_ptr.next

        fast_ptr.next = slow_ptr.next
        slow_ptr.next = self.head


my_list = CircularLinkedList()
listA = CircularLinkedList()
listB = CircularLinkedList()

my_list.pushNode(1)
my_list.pushNode(3)
my_list.pushNode(6)
my_list.pushNode(7)
my_list.printList()

my_list.split(listA, listB)
print("listA")
listA.printList()
print("listB")
listB.printList()
