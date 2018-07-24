"""program to reverse a linked list"""

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



    def reverseList(self):
        prev_ptr = None
        curr_ptr = self.head
        next_ptr = curr_ptr.next
        while curr_ptr:
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
            if next_ptr != None:
                next_ptr = next_ptr.next
        self.head = prev_ptr



if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(3)
    my_list.insertBeginning(4)
    my_list.insertBeginning(5)
    my_list.printList()
    print("reverse list")
    my_list.reverseList()
    my_list.printList()


