class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DualyList:
    def __init__(self):
        self.head = None

    def insertFront(self, item):
        new_node = Node(item)
        temp = self.head
        if self.head is None:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

        # insert at end
        elif self.head is not None:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.next = None
            new_node.prev = temp

    def insertAfter(self, given_node, item):
        new_node = Node(item)
        if given_node is None:
            return
        else:
            new_node.next = given_node.next
            new_node.prev = given_node
            given_node.next =  new_node

        if new_node.next is not None:
            new_node.next.prev = new_node



    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__=='__main__':
    my_list = DualyList()
    my_list.insertFront(1)
    my_list.insertFront(2)
    my_list.insertFront(3)
    my_list.insertAfter(my_list.head.next, 4)
    my_list.insertAfter(my_list.head, 7)
    my_list.printList()