import pytest
from data_structures.hash_table.hash_table import HashTable
from challenges.hash_tables.left_join.left_join import left_join

@pytest.fixture
def empty_hash_table_1():
    h = HashTable()
    return h

@pytest.fixture
def empty_hash_table_2():
    h = HashTable()
    return h

@pytest.fixture
def ex_hash_table_1():
    h1 = HashTable()
    h1._set('fond', 'enamored')
    h1._set('wrath', 'angered')
    h1._set('diligent', 'employed')
    h1._set('outfit', 'garb')
    h1._set('guide', 'usher')
    return h1


@pytest.fixture
def ex_hash_table_2():
    h2 = HashTable()
    h2._set('fond', 'averse')
    h2._set('wrath', 'delight')
    h2._set('diligent', 'idle')
    h2._set('guide', 'follow')
    h2._set('flow', 'jam')
    return h2


def test_module_exists():
    """Test that left_join module was imported in properly
    """
    return left_join


def test_example_works(ex_hash_table_1, ex_hash_table_2):
    """Test that left_join works with provided example
    """
    actual = left_join(ex_hash_table_1, ex_hash_table_2)
    print(actual)
    expected = [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'angered', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', None]]
    assert actual == expected


def test_empty_input(empty_hash_table_1, empty_hash_table_2):
    """Test that left_join returns an empty array when given empty hash tables as input
    """
    actual = left_join(empty_hash_table_1, empty_hash_table_2)
    expected = []
    assert actual == expected
