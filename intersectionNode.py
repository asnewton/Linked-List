
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        while self:
            return '{}->{}'.format(self.data, self.next)

class LinkedList:
    def intersectionNode(self, headA, headB):
        currA, currB = headA, headB
        lenA, lenB = 0, 0
        while currA != None:
            lenA += 1
            currA = currA.next
        while currB != None:
            lenB += 1
            currB = currB.next
        currA, currB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                currA = currA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                currB = currB.next
        while currB != currA:
            currB = currB.next
            currA = currA.next
        return currA


if __name__=='__main__':
    h1 = Node(0)
    h1.next = Node(1)
    h1.next.next = Node(2)
    h1.next.next = Node(4)
    h2 = Node(3)
    h2.next = Node(2)
    print(LinkedList().intersectionNode(h1, h2))