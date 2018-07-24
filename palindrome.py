class NewStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.stack)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    my_stack = NewStack()
    def __init__(self):
        self.head = None

    def insertBeginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def isPalindrome(self):
        temp = self.head
        while temp:
            self.my_stack.push(temp.data)
            temp = temp.next
        while temp:
            if self.my_stack.pop() == temp.data:
                return True
            else:
                return False
            temp = temp.next


if __name__=='__main__':
    my_list = LinkedList()

    my_list.insertBeginning(1)
    my_list.insertBeginning(3)
    my_list.insertBeginning(3)
    my_list.insertBeginning(1)
    print(my_list.isPalindrome())

