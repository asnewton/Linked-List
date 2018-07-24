"""Program for nth node from the end of a Linked List"""

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

    def nthNodeFromLast(self, pos):
        temp = self.head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        count = 0
        new_pos = length - pos + 1
        while temp:
            if count == new_pos:
                return temp.data
            else:
                count += 1
            temp = temp.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(3)
    my_list.insertBeginning(4)
    my_list.insertBeginning(5)
    my_list.insertBeginning(2)
    my_list.printList()
    print("nth node from last :")
    print(my_list.nthNodeFromLast(4))

