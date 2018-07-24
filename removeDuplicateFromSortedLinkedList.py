""" """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def remove_duplicate(self):
        temp = self.head
        curr = self.head
        while curr != None and curr.next != None:
            if curr.data == curr.next.data:
                temp = curr.next.next
                if temp == None:
                    curr.next = None
                    break
            if curr.data != curr.next.data:
                curr = curr.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



if __name__=='__main__':
    my_list = LinkedList()

    my_list.insert_beginning(1)
    my_list.insert_beginning(1)
    my_list.insert_beginning(2)
    my_list.insert_beginning(2)
    my_list.insert_beginning(2)
    print("before removing")
    my_list.print_list()
    my_list.remove_duplicate()
    print("after removing")
    my_list.print_list()

