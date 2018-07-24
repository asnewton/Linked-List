"""Given a singly linked list, find middle of the linked list."""
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

    def getMidNode(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr != None and fast_ptr.next != None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr.data


if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(3)
    my_list.insertBeginning(4)
    my_list.insertBeginning(5)
    my_list.insertBeginning(2)
    my_list.printList()
    print "Middle element is :",my_list.getMidNode()