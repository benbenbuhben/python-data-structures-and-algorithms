import pytest
from data_structures.linked_list.linked_list_class.linked_list import LinkedList
from challenges.linked_list.ll_merge import merge_lists
import io
import sys
from contextlib import contextmanager


@pytest.fixture
def empty_list1():
    return LinkedList()


@pytest.fixture
def empty_list2():
    return LinkedList()


@pytest.fixture
def small_list1():
    return LinkedList([1, 3, 5, 7])


@pytest.fixture
def small_list2():
    return LinkedList([2, 4, 6, 8])


@pytest.fixture
def long_list():
    return LinkedList([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])


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


def test_ll_merge_zips_two_lists_of_the_same_length(small_list1, small_list2):
    actual = merge_lists(small_list1, small_list2)
    with captured_output() as (out, err):
        print(actual)
    output = out.getvalue().strip()
    assert output == '(Head: 1) -> (Next: 2) -> (Next: 3) -> (Next: 4) -> (Next: 5) -> (Next: 6) -> (Next: 7) -> (Next: 8) -> (Next: None)'


def test_ll_merge_zips_two_lists_of_differeing_lengths(small_list1, long_list):
    actual = merge_lists(small_list1, long_list)
    with captured_output() as (out, err):
        print(actual)
    output = out.getvalue().strip()
    assert output == '(Head: 1) -> (Next: 10) -> (Next: 3) -> (Next: 11) -> (Next: 5) -> (Next: 12) -> (Next: 7) -> (Next: 13) -> (Next: 14) -> (Next: 15) -> (Next: 16) -> (Next: 17) -> (Next: 18) -> (Next: 19) -> (Next: None)'


def test_ll_merge_zips_two_empty_lists(empty_list1, empty_list2):
    actual = merge_lists(empty_list1, empty_list2)
    with captured_output() as (out, err):
        print(actual)
    output = out.getvalue().strip()
    assert output == '(Head: None)'
