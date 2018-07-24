"""Write a function that counts the number of times a given int occurs in a Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def deleteGreater(self):
        currptr = self.head
        nextptr = currptr.next
        while currptr:
            if currptr.data > nextptr.data:
                currptr = nextptr
                nextptr = nextptr.next
            if currptr.data < nextptr.data:
                currptr.next = nextptr.next



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
    print("delete greater")
    my_list.deleteGreater()
    my_list.printList()

