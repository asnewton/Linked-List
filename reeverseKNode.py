"""Reverse K nodes in a Singly Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def reverseKnodes(self, pos):
        preptr = None
        currptr = self.head
        nextptr = currptr.next
        i = 0
        while currptr and i < pos:
            currptr.next = preptr
            preptr = currptr
            currptr = nextptr
            if nextptr is not None:
                nextptr = nextptr.next
                self.head.next = currptr
            i += 1
        self.head = preptr


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(3)
    my_list.insertBeginning(4)
    my_list.insertBeginning(5)
    my_list.printList()
    print("reverse list")
    my_list.reverseKnodes(3)
    my_list.printList()



