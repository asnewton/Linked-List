class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    #function to print the content of linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    #function to insert a new node at beginning
    def insertBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    #function to insert a node after a given node
    def insertAfter(self, prev_node, item):
        new_node = Node(item)
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    #function to insert a node at the end of linked list
    def insertEnd(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


#execution of code starts here
if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(2)
    my_list.insertEnd(3)
    my_list.insertBeginning(1)
    my_list.insertEnd(4)
    my_list.insertAfter(my_list.head.next, 9)

    my_list.printList()
