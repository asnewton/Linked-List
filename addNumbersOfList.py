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

    def addnum(self, listA, listB):
        prev = None
        temp = None
        carry = 0
        while listA is not None and listB is not None:
            if listA is None:
                Adata = 0
            else:
                Adata = listA.data
            if listB is None:
                Bdata = 0
            else:
                Bdata = listB.data

            sum = Adata + Bdata + carry

            if sum > 10:
                carry = 1
            else:
                carry = 0

            if sum < 10:
                sum = sum
            else:
                sum = sum % 10

            temp = Node(sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if listA is not None:
                listA = listA.next
            if listB is not None:
                listB = listB.next

        if carry > 0:
            temp.next = carry

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


listA = LinkedList()
listB = LinkedList()
listA.insertBeginning(1)
listA.insertBeginning(9)
listA.insertBeginning(7)
print("list A")
listA.printList()
listB.insertBeginning(3)
listB.insertBeginning(4)
listB.insertBeginning(5)
print("list B")
listB.printList()
result = LinkedList()
result.addnum(listA.head, listB.head)
print("addition")
result.printList()


