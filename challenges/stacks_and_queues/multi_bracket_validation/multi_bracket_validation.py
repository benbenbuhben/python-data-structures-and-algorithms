from data_structures.stack.stack import Stack


def multi_bracket_validation(s):
    """Function that determines if brackets are balanced.
    args: a string
    output: a boolean
    """
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    stack = Stack()

    for i in range(len(s)):
        if s[i] in opening:
            stack.push(s[i])
        if s[i] in closing:
            if not len(stack):
                return False
            elif opening[closing.index(s[i])] != stack.top.value:
                return False
            else:
                stack.pop()
    if len(stack):
        return False
    else:
        return True
