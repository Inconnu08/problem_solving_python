class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class LinkList:
    __slots__ = 'head', 'size'

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.get_next()


myList = LinkList()

myList.insert(5)
myList.insert(15)
myList.insert(25)
print("Printing")
myList.print_list()
print('size', myList.get_size())
