class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    newstack = MyStack()

    def __init__(self):
        self.head = None

    def insertBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def deleteAlter(self):
        currnode = self.head
        nextnode = currnode.next
        if self.head is None:
            return

        while currnode and nextnode:
            currnode.next = nextnode.next
            currnode = currnode.next
            if currnode is not None:
                nextnode = currnode.next

    def pushToStack(self):
        currnode = self.head
        nextnode = currnode.next
        LinkedList.newstack.push(nextnode.data)
        if self.head is None:
            return

        while currnode and nextnode:
            currnode.next = nextnode.next
            currnode = currnode.next
            if currnode is not None:
                nextnode = currnode.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__=='__main__':
    my_list = LinkedList()
    my_list.insertBeginning(5)
    my_list.insertBeginning(4)
    my_list.insertBeginning(3)
    my_list.insertBeginning(2)
    my_list.insertBeginning(1)
    my_list.printList()
    print("applying delate_alter")
    my_list.deleteAlter()
    my_list.printList()
    print("applying pushToStack")
    my_list.pushToStack()
    print(LinkedList.newstack.pop())
