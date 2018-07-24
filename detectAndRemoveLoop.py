"""detect and remove loop from linked list"""

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

    def detectAndRemove(self):
        slowptr = self.head
        fastptr = self.head
        while slowptr and fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next

            if slowptr == fastptr:
                print("loop found!!")
                slowptr = self.head
                while slowptr.next != fastptr.next:
                    slowptr = slowptr.next
                    fastptr = fastptr.next
                fastptr.next = None


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


my_list = LinkedList()
my_list.insertBeginning(1)
my_list.insertBeginning(2)
my_list.insertBeginning(3)
my_list.insertBeginning(4)
my_list.insertBeginning(5)
my_list.head.next.next.next.next.next = my_list.head.next.next
my_list.detectAndRemove()
my_list.printList()



