""" Write a program to reverse a Dualy Linked List """

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DualyList:

    def __init__(self):
        self.head = None

    def insertNode(self, item):
        new_node = Node(item)
        temp = self.head
        if self.head is None:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

        # insert at end
        elif self.head is not None:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.next = None
            new_node.prev = temp

    def reverse(self):
        preptr = None
        currptr = self.head

        while currptr != None:
            preptr = currptr.prev
            currptr.prev = currptr.next
            currptr.next = preptr
            currptr = currptr.prev
        if preptr is not None:
            self.head = preptr.prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__=='__main__':
    my_list = DualyList()
    my_list.insertNode(1)
    my_list.insertNode(2)
    my_list.insertNode(3)
    my_list.insertNode(4)
    my_list.printList()
    my_list.reverse()
    print("after reversal ")
    my_list.printList()
