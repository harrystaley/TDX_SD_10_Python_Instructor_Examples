class Node:
    """
    This defines the class of a linked list node.
    """
    def __init__(self, data):
        """
        Defines the instance level parameters of a node..
        :param data: A storage location for data associated with our node.
        """
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    """
    This is the class level def of a linked list.
    """
    def __init__(self):
        self.head = None

    def create(self, val):
        """
        Add a node at the head of our linked list.
        :param val: Some data to be stored in our new node.
        :return: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        """
        Prints the linked list in order.
        :return:  None
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    linked_lst = LinkedList()
    # create nodes in our list.
    linked_lst.create(1)
    linked_lst.create(2)
    linked_lst.create(3)

    linked_lst.printlist()
