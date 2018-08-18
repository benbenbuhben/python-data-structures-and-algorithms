from .node import Node
from typing import Any


class LinkedList(object):
    def __init__(self, list=None):
        self.head = Node()
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
        return self.len

    def __str__(self):
        current_node = self.head
        output = f'(Head: {self.head})'
        while current_node:
            current_node = current_node._next
            output += f' -> (Next: {current_node})'
        return output + ''

    def insert(self, value: Any) -> Node:
        node = Node(value)
        if not self.head:
            self.head = node
            return self
        else:
            self.head, self.head._next = node, self.head
        self.len += 1

    # Type annotations
    def find(self, value: Any) -> bool:
        current_node = self.head

        while current_node:
            if current_node.val == value:
                return True
            current_node = current_node._next

        return False










