class Node:
    """docstring for Node.data"""

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """docstring for LinkedList."""

    def __init__(self):
        self.head = None
        self.current_node = None

    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
            self.current_node = self.head
            self.current_node.previous = None
        elif not self.current_node:
            self.current_node = Node(value)
            self.current_node.next = self.head
            self.head = self.current_node
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
        self.current_node = self.head

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
        current_node = self.head

        while current_node is not None:
            node_list.append(current_node)
            current_node = current_node.next

        print(node_list)

    def list_length(self):
        listLength = 0
        current_node = self.head

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

    def search(self, term):
        index = 1
        self.reset()
        while self.current_node:
            if self.current_node.data == term:
                print(f"{term} found at index {index}")
                return self.current_node
            self.next()
            index += 1

    def last_node(self):
        while self.current_node.next:
            self.next()
        return self.current_node

    def insert_node_after(self, index, datum):
        self.locate(index)
        next_node = self.current_node.next
        self.add_node(datum)
        self.current_node.next = next_node

    def insert_node_at(self, index, datum):
        self.locate(index)
        next_node = self.current_node
        self.current_node = self.current_node.previous
        self.add_node(datum)
        self.current_node.next = next_node

    def insert_at_end(self, datum):
        self.last_node()
        self.add_node(datum)

    def replace_node(self, index, datum):
        self.locate(index)
        print(self.current_node)
        self.current_node.data = datum


testList = LinkedList()
testList.build([2, 4, 6, 8, 10, 12, 14, 16, 18])
testList.insert_node_after(5, 22)
testList.insert_node_at(1, 17)
testList.replace_node(5, 15)
testList.search(15)
print(testList.locate(1))
testList.list_print()
print(testList.current_node)
testList.next()
print(testList.current_node)
testList.insert_at_end(78)
testList.list_print()
