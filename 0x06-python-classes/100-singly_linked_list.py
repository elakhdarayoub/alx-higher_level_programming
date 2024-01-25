#!/usr/bin/python3
"""A singly linked list module"""


class Node:
    """This class of the singly linked list node"""

    """the Constructor function"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """Data getter"""
    @property
    def data(self):
        return self.__data

    """Data setter"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """Next_node getter"""
    @property
    def next_node(self):
        return self.__next_node

    """Next_node setter"""
    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node)) or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The class constructor"""
    def __init__(self):
        self.__head = None

    """inserting nodes in a sorted order"""
    def sorted_insert(self, value):
        new = Node(value)

        if self.__head is None:
            self.head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

        """Print the linked list"""
        def __str__(self):
            tmp = self.__head
            while tmp is not None:
                print("{}".format(tmp.data))
                tmp = tmp.next_node
