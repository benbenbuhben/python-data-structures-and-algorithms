import pytest
from .linked_list import LinkedList
import io
import sys
from contextlib import contextmanager


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    return LinkedList([1, 2, 3, 4])


@contextmanager
def captured_output():
    '''Helper function for testing stdout'''
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def test_this_file_works():
    pass


def test_linked_list_module_exists():
    return LinkedList


def test_small_list_exists(small_list):
    return small_list


def test_default_properties(empty_list):
    print(empty_list.head)
    assert empty_list.head is None
    assert empty_list.len is 0


def test_prepend_successful(empty_list):
    empty_list.prepend(25)
    assert empty_list.head.val is 25


def test_length_of_list_increases_upon_prepend(empty_list):
    assert len(empty_list) is 0
    empty_list.prepend(25)
    assert len(empty_list) is 1


def test_find_returns_true_if_value_exists(small_list):
    actual = small_list.find(4)
    assert actual is True


def test_find_returns_false_if_value_dne(small_list):
    actual = small_list.find(5)
    assert actual is False


def test_print_function_works(small_list):
    with captured_output() as (out, err):
        print(small_list)
    output = out.getvalue().strip()
    assert output == '(Head: 1) -> (Next: 2) -> (Next: 3) -> (Next: 4) -> (Next: None)'


def test_append_increases_length(small_list):
    initialLength = len(small_list)
    small_list.append(5)
    assert len(small_list) == initialLength + 1


def test_append_places_value_at_end_of_list(small_list):

    current = small_list.head
    while current._next:
        current = current._next
    initialEnd = current.val
    assert initialEnd == 4

    small_list.append(5)

    current = small_list.head
    while current._next:
        current = current._next
    modifiedEnd = current.val
    assert modifiedEnd == 5


def test_insert_after_increases_length(small_list):
    initialLength = len(small_list)
    small_list.insertAfter(2, 5)
    assert len(small_list) == initialLength + 1


def test_insert_after_provides_feedback_if_val_not_found(small_list):
    with captured_output() as (out, err):
        small_list.insertAfter(12, 5)
    output = out.getvalue().strip()
    assert output == 'Linked List does not contain the search value'


def test_insert_before_increases_length(small_list):
    initialLength = len(small_list)
    small_list.insertBefore(2, 5)
    assert len(small_list) == initialLength + 1


def test_insert_before_modifies_list_as_expected(small_list):
    small_list.insertBefore(2, 5)
    with captured_output() as (out, err):
        print(small_list)
    output = out.getvalue().strip()
    assert output == '(Head: 1) -> (Next: 5) -> (Next: 2) -> (Next: 3) -> (Next: 4) -> (Next: None)'


def test_kth_from_end_returns_value_kth_from_end(small_list):
    expected = 3
    actual = small_list.kth_from_end(2)
    assert expected == actual


def test_kth_from_end_raises_exception_with_negative_input(small_list):
    with pytest.raises(Exception) as e_info:
        small_list.kth_from_end(-6)


def test_kth_from_end_raises_exception_with_input_greater_than_list_length(small_list):
    with pytest.raises(Exception) as e_info:
        small_list.kth_from_end(29186)
