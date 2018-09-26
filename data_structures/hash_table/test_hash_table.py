import pytest
from .hash_table import HashTable
import io
import sys
from contextlib import contextmanager


@pytest.fixture
def empty_hash_table():
    """Fixture that returns an empty hash table
    """
    return HashTable()


@pytest.fixture
def populated_hash_table():
    """Fixture that returns a populated hash table
    """
    h = HashTable()
    h._set('Ben', 6185305358)
    h._set('Spencer', 8329352930)
    h._set('Tim', 6176350989)
    h._set('Suzie', 9652351188)
    return h


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
    """Testing that this file is read in by pytest
    """
    pass


def test_hash_table_module_exists():
    """Function to test that the hash table module was imported properly
    """
    return HashTable


def test_empty_hash_table_exists(empty_hash_table):
    """Test existence of empty hash table fixture
    """
    return empty_hash_table


def test_default_properties(empty_hash_table):
    """Test default properties on empty hash table
    """
    assert empty_hash_table.size == 8192
    assert empty_hash_table.hashtable == [None] * empty_hash_table.size


def test_populated_hash_table_exists(populated_hash_table):
    """Test populated hash table fixture exists
    """
    return populated_hash_table


def test_get_works(populated_hash_table):
    """Test get method on hash table class returns expected value
    """
    value = populated_hash_table._get('Ben')
    assert value == 6185305358


def test_setting_a_new_value(populated_hash_table):
    """Test set method on puts a key value pair into the hash table
    """
    populated_hash_table._set('Lorenzo', 9264950271)
    value = populated_hash_table._get('Lorenzo')
    assert value == 9264950271


def test_deleting_a_key(populated_hash_table):
    """Test delete method removes the key/value from the database and returns the value.
    """
    populated_hash_table._set('Cisco', 1234567891)
    deleted_value = populated_hash_table._remove('Cisco')
    assert deleted_value == 1234567891
    assert populated_hash_table._get('Cisco') is None


def test_len_works(populated_hash_table):
    """Test magic method len() works as expected
    """
    assert len(populated_hash_table) == 4

