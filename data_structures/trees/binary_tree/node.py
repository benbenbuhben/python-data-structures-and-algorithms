class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | Val: {self.val} | Left: {self.left} | Right: {self.right}>'
