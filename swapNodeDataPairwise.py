"""write a program to swap node data of linked list pairwise"""

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

    def swap_pairwise(self):
        temp = self.head
        while temp != None and temp.next != None:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    my_list = LinkedList()

    my_list.insert_beginnig(1)
    my_list.insert_beginnig(3)
    my_list.insert_beginnig(4)
    my_list.insert_beginnig(5)
    my_list.printList()
    my_list.swap_pairwise()
    print("after swapping")
    my_list.printList()