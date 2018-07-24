"""Write a function to remove a duplicate of a sorted linked list"""
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

    def removeDuplicate(self):
        ptr1 , ptr2, dup = self.head, self.head, self.head
        while (ptr1 != None and ptr1.next != None):
            ptr2 = ptr1
            while ptr2.next != None:
                if ptr1.data == ptr2.next.data:
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


"""
    def removeDuplicate(self):
        temp = self.head
        prev = self.head
        while temp.next != None:
            if temp.data == temp.next.data:
                prev = temp.next.next
                temp.next = prev
            temp = temp.next
"""




if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(1)
    my_list.insertBeginning(2)
    my_list.insertBeginning(2)
    my_list.insertBeginning(2)

    my_list.printList()
    print("after removing duplicates")
    my_list.removeDuplicate()
    my_list.printList()