class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size

    def insertHead(self, item):
        new_node = Node(item)
        self.head = new_node
        self.size += 1



    def insertTail(self, item):
        new_node = Node(item)
        current = self.head

        if self.head == None:
            self.head = new_node

        while current:
            current = current.next
        current.next = new_node
        

    """
    def sortedInsert(self, item):
        new_node = Node(item)
        current = self.head

        if self.head == None:
            self.head = new_node

        if current == None or current.value > item:
            new_node.next = self.head
            self.head = new_node
            return
        
        while current.next != None and current.next.value < item:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    """

    def printList(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next

my_list = LinkedList()
print "size is ", my_list.length()
print(my_list.printList())
my_list.insertTail(2)
print(my_list.is_empty())