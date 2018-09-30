from .node import Node


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def pre_order(self):

        results = []

        def _walk(node):
            results.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)

        return results

    def post_order(self):

        results = []

        def _walk(node):

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            results.append(node.value)

        _walk(self.root)

        return results

    def in_order(self):

        results = []

        def _walk(node):

            if node.left:
                _walk(node.left)

            results.append(node.value)

            if node.right:
                _walk(node.right)

        _walk(self.root)

        return results
