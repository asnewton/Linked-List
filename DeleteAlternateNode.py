"""program to delete alternate nodes of a Linked List"""

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

    def deleteAlter(self):
        curr = self.head

        while curr.next:
            temp = curr.next
            curr.next = temp.next
            curr = temp.next
            if curr is not None:
                temp = curr.next


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



if __name__=='__main__':
    my_list = LinkedList()
    my_list.insertBeginning(9)
    my_list.insertBeginning(3)
    my_list.insertBeginning(4)
    my_list.insertBeginning(5)
    my_list.insertBeginning(2)
    my_list.printList()
    print("after deletion")
    my_list.deleteAlter()
    my_list.printList()

    """
    def pushInStack(self):
        curr = self.head

        while curr.next:
            temp = curr.next
            curr.next = temp.next
            curr = temp.next
            LinkedList.newstack.push(.data)
            if curr is not None:
                temp = curr.next
    """