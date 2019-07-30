class Node:
    """docstring for Node.data"""

    def __init__(self, data=0):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """docstring for LinkedList."""

    def __init__(self):
        self.head_value = None

    def build(self, array):
        array = array
        self.head_value = array[0]
        current_node = Node(self.head_value)

        for key, value in enumerate(array[1::], 1):
            current_node.next = Node(value)
            current_node = current_node.next
            print(current_node)

    def listPrint(self):
        node_list = []
        current_node = self.head_value

        while current_node is not None:
            node_list.append(current_node)
            current_node = current_node.next

        return node_list

    def listLength(self):
        listLength = 0
        current_node = self.head_value

        while current_node:
            listLength += 1
            current_node = current_node.next

        return listLength


testList = LinkedList()
testList.build([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(testList.listPrint())
