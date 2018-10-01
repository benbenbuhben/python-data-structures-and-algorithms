import pytest
from data_structures.hash_table.hash_table import HashTable
from data_structures.trees.binary_tree.binary_tree import BinaryTree
from data_structures.trees.binary_tree.node import Node
from challenges.hash_tables.tree_intersection.tree_intersection import tree_intersection

@pytest.fixture
def empty_tree_1():
    return BinaryTree()

@pytest.fixture
def empty_tree_2():
    return BinaryTree()

@pytest.fixture
def populated_tree_1():
    n1 = Node(150)
    n2 = Node(100)
    n3 = Node(250)
    n4 = Node(75)
    n5 = Node(160)
    n6 = Node(200)
    n7 = Node(350)
    n8 = Node(125)
    n9 = Node(175)
    n10 = Node(300)
    n11 = Node(500)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9
    n7.left = n10
    n7.right = n11

    bt = BinaryTree(n1)

    return bt

@pytest.fixture
def populated_tree_2():
    n1 = Node(42)
    n2 = Node(100)
    n3 = Node(600)
    n4 = Node(15)
    n5 = Node(160)
    n6 = Node(200)
    n7 = Node(350)
    n8 = Node(125)
    n9 = Node(175)
    n10 = Node(4)
    n11 = Node(500)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9
    n7.left = n10
    n7.right = n11

    bt = BinaryTree(n1)

    return bt


def test_module_exists():
    """Test that module was imported in properly.
    """
    return tree_intersection


def test_function_works_for_empty_trees(empty_tree_1, empty_tree_2):
    """Test that tree_intersection returns an empty array when given empty trees
    """
    actual = tree_intersection(empty_tree_1, empty_tree_2)
    expected = []

    return actual == expected


def test_function_works_for_provided_example(populated_tree_1, populated_tree_2):
    """Test that tree_intersection returns an array with common values
    """
    actual = tree_intersection(populated_tree_1, populated_tree_2)
    expected = [100, 160, 200, 350, 125, 175, 4, 500]

    return sorted(actual) == sorted(expected)









