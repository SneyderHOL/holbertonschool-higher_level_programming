#!/usr/bin/python3
"""  SinglyLinkedList Class
    Attributes:
        __head (int): The data of the Node object.

"""


class SinglyLinkedList:
    """__init__: method to initilize object's properties."""
    def __init__(self):
        self.head = None

    """head: method to get the head attribute of the singly linked list

    Return:
        The return value: The Node head

    """
    @property
    def head(self):
        return self.__head

    """head: method to modify the head attribute

    Args:
        value (Node): The node object to asign.

    Raises:
        TypeError: if value is not None or is not a Node

    """
    @head.setter
    def head(self, value):
        if (value is not None and type(value) != Node):
            raise TypeError('next_node must be a Node object')
        self.__head = value

    """sorted_insert: method that inserts a new Node into the correct sorted
        position in the list(increasing order)
    """
    def sorted_insert(self, value):
        new_node = Node(value)
        aux = self.head
        tmp = self.head
        while (aux is not None and aux.data < value):
            tmp = aux
            aux = aux.next_node
        if self.head is None:
            self.head = new_node
        else:
            if aux == self.head:
                new_node.next_node = aux
                self.head = new_node
            else:
                tmp.next_node = new_node
                if aux is not None:
                    new_node.next_node = aux

    """__str__: method that converts the list in a string

    Return:
        The return value: The Node's integer value
    """
    def __str__(self):
        str_list = ''
        aux_node = self.head
        while (aux_node is not None):
            str_list += str(aux_node.data)
            if aux_node.next_node is not None:
                str_list += '\n'
            aux_node = aux_node.next_node
        return str_list

"""  Node Class
    Attributes:
        __data (int): The data of the Node object.
        __next_node (Node): The next_node of the Node object.

"""


class Node:
    """__init__: method to initilize object's properties.

    Args:
        data (int): The data of the Node object to initialize.
        next_node (Node): The next_node of the Node object to initialize.

    Raises:
        TypeError: if size is not an integer or if position is not a tuple

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """data: method to get the data attribute

    Return:
        The return value: The Node data

    """
    @property
    def data(self):
        return self.__data

    """data: method to modify the data attribute

    Args:
        value (int): The data of the Node object to modify.

    Raises:
        TypeError: if data is not an integer

    """
    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    """next_node: method to get the next_node attribute

    Return:
        The return value: The Node's next_node

    """
    @property
    def next_node(self):
        return self.__next_node

    """next_node: method to modify the next_node attribute

    Args:
        value (Node): The next_node of the Node object to modify.

    Raises:
        TypeError: if value is not a Node or is not None

    """
    @next_node.setter
    def next_node(self, value):
        if (value is not None and type(value) != Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

    """__str__: method to convert the content of the node to string

    Return:
        The return value: The Node's integer value

    """
    def __str__(self):
        return str(self.__data)
