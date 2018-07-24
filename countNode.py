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

    def getCount(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count

    """count no. of node using recurtion """
    def getCountRec(self, Node):
        if not Node:
            return 0
        else:
            return 1 + self.getCountRec(Node.next)

    """wrapping function for recurtion"""
    def getCountR(self):
        return self.getCountRec(self.head)

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
    my_list.printList()
    print "No. of nodes :",my_list.getCount()
    print "No. of nodes by recurtion :",my_list.getCountR()
