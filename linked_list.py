class Node:
    """docstring for Node.data"""

    def __init__(self, data=0):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """docstring for LinkedList."""

    def __init__(self):
        self.head_value = None
        self.current_node = None

    def add_node(self, value):
        if not self.head_value:
            self.head_value = Node(value)
            self.current_node = self.head_value
            self.current_node.previous = None
        else:
            new_node = Node(value)
            previous = self.current_node
            self.current_node.next = new_node
            self.current_node = new_node
            self.current_node.previous = previous

    def build(self, array):
        for element in array:
            self.add_node(element)
        self.reset()

    def reset(self):
        self.current_node = self.head_value

    def next(self):
        if self.current_node:
            self.current_node = self.current_node.next
            return self.current_node
        else:
            return None

    def previous(self):
        if self.current_node:
            self.current_node = self.current_node.previous
            return self.current_node
        else:
            return None

    def list_print(self):
        node_list = []
        current_node = self.head_value

        while current_node is not None:
            node_list.append(current_node)
            current_node = current_node.next

        print(node_list)

    def list_length(self):
        listLength = 0
        current_node = self.head_value

        while current_node:
            listLength += 1
            current_node = current_node.next

        return listLength

    def locate(self, n):
        index = 1
        self.reset()
        while index < n:
            self.next()
            index += 1
        return self.current_node

    def last_node(self):
        while self.current_node.next:
            self.next()
        return self.current_node


testList = LinkedList()
testList.build([2, 4, 6, 8, 10, 12, 14, 16, 18])
print(testList.list_print())
print(testList.current_node)
print(testList.current_node.next)
print(testList.last_node())
print(testList.current_node)
print(testList.locate(5))
print(testList.current_node)
