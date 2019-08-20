class Node:
    """
    Generates a new Node object

    Attributes:
        self.data (data): stores Node values, defaults to 0 if no value passed
        self.next (Node): link to next Node object
        self.previous (Node): link to previous Node object
    """

    def __init__(self, data=None):
        """
        Node init Method

        Args:
            data (data): defaults to None of no values passed
        """

        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """
    Generates an empty LinkedList object

    Attributes:
        self.head (Node): First Node object in the LinkedList
        self.current_node (Node): Current Node object being accessed
    """

    def __init__(self):
        self.head = None
        self.current_node = None

    def add_node(self, value, next_node=None):
        """
        Method to add Nodes to LinkedList
            - Nodes are added in place. No value is returned

        Args:
            data (data): values to be written to Nodes
            next_node (Node): Defaults to end of LinkedList, Node linked to node.next
        """

        if not self.head:  # if head node does not exist
            self.head = Node(value)
            self.current_node = self.head
            self.current_node.previous = None
        elif not self.current_node:  # if inserting to "left" of head
            self.current_node = Node(value)
            self.current_node.next = self.head
            self.head = self.current_node
            self.current_node.previous = None
        else:
            new_node = Node(value)
            previous_node = self.current_node
            self.current_node.next = new_node
            self.current_node = new_node
            self.current_node.next = next_node
            self.current_node.previous = previous_node

    def build(self, array):
        """
        Method to populate LinkedList
            - Generates Nodes and assigns links from a given array

        Args:
            array (array): an array of values to be linked in LinkedList
        """

        for element in array:
            self.add_node(element)
        self.reset()

    def reset(self):
        """
        Method to reset position to start of LinkedList
        """
        self.current_node = self.head

    def next(self):
        """
        Method to traverse LinkedList
            - Sets current_node to the next Node in the LinkedList
            - Returns Node object being accessed or None
        """

        if self.current_node:
            self.current_node = self.current_node.next
            return self.current_node
        else:
            return None  # returns None if Node does not exist

    def previous(self):
        """
        Method to traverse LinkedList
            - Sets current_node to the previous Node in the LinkedList
            - Returns Node object being accessed or None
        """

        if self.current_node:
            self.current_node = self.current_node.previous
            return self.current_node
        else:
            return None  # return None if Node does not exist

    def list_print(self):
        """
        Method to print out all Node values in LinkedList
            - Print() is called. No values are returned
        """

        node_list = []
        self.reset()

        while self.current_node:
            node_list.append(self.current_node)
            self.next()

        self.reset()
        print(node_list)

    def list_length(self):
        """
        Method to return number of Nodes in the LinkedList
            - Returns listLength (int)
        """

        listLength = 0
        self.reset()

        while self.current_node:
            listLength += 1
            self.next()

        return listLength

    def locate(self, index):
        """
        Method to return the Node object located at the specified index
            - Indexing starts at 1
            - Sets current_node to located Node
            - Returns Node object

        Args:
            index (int): index position of Node object to be accessed
        """

        node_index = 1
        self.reset()

        while node_index < index:
            self.next()
            node_index += 1

        return self.current_node

    def search(self, value):
        """
        Method to search LinkedList for a Node with specified value
            - Indexing starts at 1
            - Sets current_node to found Node
            - Returns found Node object

        Args:
            value (data): value of Node to be located. Will only match exact values
        """

        node_index = 1
        self.reset()

        while self.current_node:
            if self.current_node.data == value:
                print(f"{value} found at index {node_index}")
                return self.current_node
            self.next()
            node_index += 1

    def last_node(self):
        """
        Method to traverse LinkedList to last Node
            - Sets current_node to last_node
        """
        while self.current_node.next:  # traverse list until next_node is None
            self.next()

    def insert_node_after(self, index, data):
        """
        Method to insert node after given index
            - Current_node is set to new Node
            - Node is added in place. No values are returned

        Args:
            index (int): index position of previous Node
            data (data): value to be assigned to inserted Node
        """

        self.locate(index)
        next_node = self.current_node.next
        self.add_node(data, next_node)

    def insert_node_at(self, index, data):
        """
        Method to insert Node at a specified index
            - Current_node is set to new Node
            - Node is added in place. No values are returned

        Args:
            index (int): index position of new Node
            data (data): data to be asigned to Node
        """

        self.locate(index)
        next_node = self.current_node
        self.current_node = self.current_node.previous
        self.add_node(data, next_node)

    def insert_at_end(self, data):
        """
        Method to insert Node at end of LinkedList
            - Sets current_node to new Node
            - Node is added in place. No values are returned

        Args:
            data (data): data to be asigned to Node

        """

        self.last_node()
        self.add_node(data)

    def replace_node(self, index, data):
        """
        Method to replace an existing Node with a new Node
            - Method does not create a new Node object. Existing values of target Node
              are overwritten with new data
            - Replacement occurs in place. No values are returned

        Args:
            index (int): index position of Node to be replaced
            data (data): data to be assigned to Node
        """

        self.locate(index)
        self.current_node.data = data

    def remove_node(self, index):
        """
        Method to remove a Node from the LinkedList
            - Method removes Node in place. No values are returned

        Args:
            index (int): index position of the Node to be removed
        """
        self.locate(index)

        if self.current_node is self.head:
            self.head = self.current_node.next
            self.head.previous = None
        elif self.current_node.next:
            next_node = self.current_node.next
            self.current_node = self.current_node.previous
            self.current_node.next = next_node
            next_node.previous = self.current_node
        else:
            self.current_node = self.current_node.previous
            self.current_node.next = None


test_list = LinkedList()
test_list.build([1, 2, 3, 4, 5, 6, 7, 8, 9])
test_list.list_print()
test_list.remove_node(5)
test_list.list_print()
test_list.remove_node(1)
test_list.list_print()
test_list.remove_node(a)
test_list.list_print()
test_list.last_node()
print(test_list.current_node)
