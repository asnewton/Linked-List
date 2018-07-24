class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    #this function prints the content of linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


#execution of code starts here
if __name__=='__main__':
    my_list = LinkedList()

    #creating nodes
    my_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    #linking node
    my_list.head.next = second
    second.next = third

    my_list.printList()