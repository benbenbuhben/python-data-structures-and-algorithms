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
    assert empty_list.head.val is None
    assert empty_list.len is 0


def test_insertion_successful(empty_list):
    empty_list.insert(25)
    assert empty_list.head.val is 25


def test_length_of_list_increases_upon_insertion(empty_list):
    assert len(empty_list) is 0
    empty_list.insert(25)
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
