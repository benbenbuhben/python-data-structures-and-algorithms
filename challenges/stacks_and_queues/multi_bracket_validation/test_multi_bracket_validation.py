import pytest
from .multi_bracket_validation import multi_bracket_validation


def test_function_exists():
    """Check that we imported everything properly
    """
    assert multi_bracket_validation


def test_validates_balanced_brackets():
    """Function to test simple validation case
    """
    sample_string = '([\{\}])'
    assert multi_bracket_validation(sample_string) == True


def test_validates_unbalanced_brackets():
    """Function to test case with unbalanced brackets
    """
    sample_string = '([\{\}]))'
    assert multi_bracket_validation(sample_string) == False


def test_works_on_empty_string():
    """Function to test empty string (technically balanced)
    """
    sample_string = ''
    assert multi_bracket_validation(sample_string) == True


def test_works_on_closing_bracket_first():
    """Test edge case where a closing bracket is encountered first
    """
    sample = 'sdjhb)()'
    assert multi_bracket_validation(sample) == False


def test_works_on_complicated_cases():
    """Test crazy test case with balanced brackets
    """
    sample = 'asj(asjb[adksbj]akdjns()[(rg)])sd'
    assert multi_bracket_validation(sample) == True


def test_works_on_all_opening_brackets():
    """Test edge case with all opening brackets
    """
    sample = '([([([[[[((('
    assert multi_bracket_validation(sample) == False
