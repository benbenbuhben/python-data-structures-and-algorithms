class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

    def __repr__(self):
        pass

    def __str__(self):
        pass


class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

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
        """
        """
        tmp = self.top
        self.top = tmp._next
        tmp._next = None

        self._length -= 1
        return tmp.value

    def peek(self):
        """
        """
        return self.top
