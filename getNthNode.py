"""Write a GetNth() function that takes a linked list and an integer index and
returns the data value stored in the node at that index position."""

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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    #function to get nth node
    def getNode(self, pos):
        temp = self.head
        count = 0
        while temp:
            if count == pos:
                return temp.data
            else:
                count += 1
            temp = temp.next


if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(3)
    my_list.insertBeginning(4)
    my_list.insertBeginning(5)
    my_list.printList()
    print "nth node ", my_list.getNode(1)