class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # function to insert a new node at beginning
    def insertBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    #function to delete the node
    def deleteNode(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            return

        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next

    #this function prints the content of linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        if self:
            return '{}->{}'.format(self.data, self.next)

#execution of code starts here
if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(2)
    my_list.insertBeginning(3)
    my_list.insertBeginning(1)
    my_list.insertBeginning(4)
    print("before deletion")
    my_list.printList()

    print("after deletion")
    my_list.deleteNode(4)
    my_list.printList()
    my_list