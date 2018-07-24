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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def countFrequency(self, item):
        frequency = 0
        temp = self.head
        while temp:
            if temp.data == item:
                frequency += 1
            temp = temp.next
        return frequency


if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(2)
    my_list.insertBeginning(2)
    my_list.insertBeginning(1)
    my_list.insertBeginning(1)
    my_list.insertBeginning(3)
    my_list.insertBeginning(2)
    my_list.insertBeginning(3)

    my_list.printList()
    print "no. of item :",my_list.countFrequency(3)

