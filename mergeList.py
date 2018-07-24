
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.data, self.next)


class LinkedList:

    def merge_lists(self, list1, list2):
        dummy = Node(0)
        temp = dummy
        while list1 != None and list2 != None:
            if list1.data <= list2.data:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1 is None:
            temp.next = list2
        else:
            temp.next = list1

        return dummy.next


if __name__=='__main__':
    l1 = Node(0)
    l1.next = Node(1)
    l2 = Node(3)
    l2.next = Node(2)
    print(LinkedList().merge_lists(l1, l2))


"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
       
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode(3)
    l2.next = ListNode(3)
    print Solution().mergeTwoLists(l1, l2)
    """
