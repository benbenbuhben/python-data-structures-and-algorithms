from data_structures.linked_list.linked_list_class.linked_list import LinkedList


def merge_lists(ll1, ll2):
    """This function takes two linked lists and returns a linked list with nodes corresponding to the 2 input lists' nodes interleaved.
    """
    current1 = ll1.head
    current2 = ll2.head
    answer = LinkedList()
    while current1 or current2:
        if current1:
            answer.append(current1.val)
            current1 = current1._next
        if current2:
            answer.append(current2.val)
            current2 = current2._next

    return answer
