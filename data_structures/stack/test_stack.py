from .stack import Stack
import pytest
import io
import sys
from contextlib import contextmanager


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


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

def test_stack_class_exists():
    """Test that the stack module was properly imported
    """
    assert Stack


def test_can_instantiate_empty_stack(empty_stack):
    """Test that test fixture is of the expected class
    """
    assert isinstance(empty_stack, Stack)


def test_insertion_of_value_increases_length(empty_stack):
    assert len(empty_stack) == 0
    empty_stack.push(100)
    assert len(empty_stack) == 1


def test_default_value_of_top(empty_stack):
    assert empty_stack.top is None


def test_small_stack_gets_built_as_expected(small_stack):
    with captured_output() as (out, err):
        print(small_stack)
    output = out.getvalue().strip()
    assert output == '(Head: 4) -> (Next: 3) -> (Next: 2) -> (Next: 1) -> (Next: None)'
