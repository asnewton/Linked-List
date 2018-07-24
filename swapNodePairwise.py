"""write a program to swap node pairwise in linked list"""

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

    def swap_node(self):
        curr = self.head

        while curr.next:
            if curr is None or curr.next is None:
                return
            else:
                forw = curr.next
                temp = forw.next
                forw.next = curr
                curr.next = temp.next
                curr = temp
            curr = curr.next



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
    my_list.swap_node()
    print("after swapping")
    my_list.printList()