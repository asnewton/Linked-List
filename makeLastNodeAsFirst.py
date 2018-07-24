"""Program to move last element to front of a given Linked List."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginnig(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def moveLast(self):
        last = self.head
        while last.next != None:
            secLast = last
            last = last.next

        secLast.next = None
        last.next = self.head
        self.head = last




if __name__=='__main__':
    my_list = LinkedList()

    my_list.insert_beginnig(1)
    my_list.insert_beginnig(3)
    my_list.insert_beginnig(4)
    my_list.insert_beginnig(5)
    my_list.printList()
    my_list.moveLast()
    print("after moving")
    my_list.printList()

