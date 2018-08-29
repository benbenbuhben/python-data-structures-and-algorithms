from .node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __repr__(self):
        pass

    def __str__(self):
        """Magic Method that returns a nicely formatted display of LinkedList
        """
        current_node = self.top
        output = f'(Head: {self.top})'
        while current_node:
            current_node = current_node._next
            output += f' -> (Next: {current_node})'
        return output + ''

    def __len__(self):
        """Magic method to return length of LinkedList
        """
        return self._length

    def push(self, value):
        """Method which accepts a value of any type and creates a new Node in the Stack instance.

            Args:
                value (object): Any

            Return: Node
        """
        self.top = Node(value, self.top)

        self._length += 1

        return self.top

    def pop(self):
        """Method that removes and returns top value in the stack.
        """
        tmp = self.top
        self.top = tmp._next
        tmp._next = None

        self._length -= 1
        return tmp.value

    def peek(self):
        """Method to see what the queue looks like. Should this return a value or a node?
        """
        return self.top
