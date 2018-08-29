from ...data_structures.stack.stack import Stack


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val):
        """
        """
        self.front = self.stack2.push(val)
        self.length += 1
        return self

    def dequeue(self):
        """
        """
        while self.stack2.length > 1:
            self.stack1.push(self.stack2.pop())

        output = self.stack2.pop()

        while self.stack1.length:
            self.stack2.push(self.stack1.pop())

        self.front = self.stack2
        self.length += 1

        return output
