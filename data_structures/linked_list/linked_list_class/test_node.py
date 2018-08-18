import pytest
from .node import Node


@pytest.fixture
def empty_node():
    return Node()


@pytest.fixture
def single_node():
    return Node(5)


def test_this_file_works():
    pass


def test_node_module_exists():
    return Node


def test_node_exists(single_node):
    return single_node


def test_default_properties_empty(empty_node):
    assert empty_node.val is None
    assert empty_node._next is None


def test_properties_single_node(single_node):
    assert single_node.val == 5
    assert single_node._next is None
