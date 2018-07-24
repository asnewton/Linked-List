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
        while temp != None:
            print(temp.data)
            temp = temp.next

    def deleteAtPosition(self, pos):
        if self.head is None:
            return

        if pos == 0:
            self.head = self.head.next

        temp = self.head
        prev = self.head
        i = 0
        while i < pos - 1 and temp.next is not None:
            prev = temp
            temp = temp.next
            i += 1

        if temp is None or temp.next is None:
            return

        prev.next = temp.next


if __name__=='__main__':
    my_list = LinkedList()
    my_list.insertBeginning(2)
    my_list.insertBeginning(4)
    my_list.insertBeginning(5)
    my_list.insertBeginning(7)
    print("before deletion")
    my_list.printList()
    print("after deletion")
    my_list.deleteAtPosition(3)
    my_list.printList()
