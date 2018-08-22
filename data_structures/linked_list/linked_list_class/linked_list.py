from .node import Node
from typing import Any


class LinkedList(object):
    def __init__(self, list=None):
        """Constructor function for LinkedList class
        """
        self.head = None
        self.len = 0

        if list:
            self.head = Node(list[0])
            current_node = self.head
            self.len += 1
            for i in list[1:]:
                current_node._next = Node(i)
                current_node = current_node._next
                self.len += 1

    def __len__(self):
        """Magic method to return length of LinkedList
        """
        return self.len

    def __str__(self):
        """Magic Method that returns a nicely formatted display of LinkedList
        """
        current_node = self.head
        output = f'(Head: {self.head})'
        while current_node:
            current_node = current_node._next
            output += f' -> (Next: {current_node})'
        return output + ''

    def prepend(self, value):
        """Adds value to front of LinkedList
        """
        self.head = Node(value, self.head)
        self.len += 1

    def append(self, value):
        """Adds value to end of LinkedList
        """
        current = self.head

        while current._next:
            current = current._next

        node = Node(value)
        current._next = node

        self.len += 1

    def insertBefore(self, value, newVal):
        """Finds value and inserts newVal before it
        """
        child = None
        parent = None
        current = self.head

        while current and current.val != value:
            parent, child = current, current._next
            current = current._next

        if current:
            newParent = Node(newVal, child)
            parent._next = newParent
            self.len += 1

        else:
            print('Linked List does not contain the search value')

    def insertAfter(self, value, newVal):
        """Finds value and inserts newVal after it
        """
        current = self.head

        while current and current.val != value:
            current = current._next

        if current:
            child = Node(newVal, current._next)
            current._next = child
            self.len += 1

        else:
            print('Linked List does not contain the search value')

    # Type annotations
    def find(self, value):
        """Searches for input value and returns True/False corresponding to whether value exists in LinkedList
        """
        current_node = self.head

        while current_node:
            if current_node.val == value:
                return True
            current_node = current_node._next

        return False

    def kth_from_end(self, k):
        """Finds and returns value of node that k nodes from the end of the linked list
        """
        current = self.head
        values = []

        while current:
            values += [current.val]
            current = current._next

        return values[-k]
