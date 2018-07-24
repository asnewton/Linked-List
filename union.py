class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def union(self, list1, list2):
        p = self.head
        q = self.head
        r = None
        flag = 0
        while p!= None:
            p = p.next
            while q != None:
                r = list1
                if r.data == q.data:
                    flag = 1
                    break
                r = r.next

            if flag == 1:
                q = q.next
                flag = 0
            else:
                p.next = q
                p = p.next
                p.next = None
                q = q.next
        self.head = p

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



if __name__=='__main__':
    my_list = LinkedList()

    l1 = Node(0)
    l1.next = Node(1)
    l2 = Node(3)
    l2.next = Node(2)
    print(my_list.union(l1, l2))

