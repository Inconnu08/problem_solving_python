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
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

