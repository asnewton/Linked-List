class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyList:
    def __init__(self , head = None, tail = None):
        self.head = head
        self.tail = tail
        self.count = 0

    def length(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def addHead(self, item):
        new_node = Node(item)

        if self.head == None:
            self.head = new_node
        else:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1




my_list = DoublyList()
print(my_list.is_empty())
print(my_list.length())