from .node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self._length = 0

    def __repr__(self):
        pass

    def __str__(self):
        """Magic Method that returns a nicely formatted display of LinkedList
        """
        current_node = self.front
        output = f'(Head: {self.front})'
        while current_node:
            current_node = current_node._next
            output += f' -> (Next: {current_node})'
        return output + ''

    def __len__(self):
        """Magic method to return length of LinkedList
        """
        return self._length

    def enqueue(self, value):
        """Method which accepts a value of any type and creates a new Node in the Queue instance.

            Args:
                value (object): Any

            Return: Node
        """
        if not self.front:
          self.front = Node(value)
        else:
          newNode = Node(value)
          current = self.front
          while current._next:
            current = current._next
          current._next = newNode
          # self.front = Node(self.front, newNode)
          self.back = Node(value)

        self._length += 1

        return self.front

    def dequeue(self):
        """
        """
        tmp = self.front
        self.front = tmp._next
        tmp._next = None

        self._length -= 1
        return tmp.value

    def peek(self):
        """
        """
        return self.front
