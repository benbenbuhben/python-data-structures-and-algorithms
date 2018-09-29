import pytest
from challenges.hash_tables.repeated_word.repeated_word import repeated_word


def test_module_exists():
    """Test that repeated_word module was imported in properly
    """
    return repeated_word


def test_short_example_works():
    """Test that repeated_word works on small string
    """
    text = 'Once upon a time, there was a brave princess who...'
    actual = repeated_word(text)
    expected = 'a'
    assert actual == expected


def test_long_example_works():
    """Test that repeated_word works on long string
    """
    text = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    actual = repeated_word(text)
    expected = 'it'
    assert actual == expected


def test_example_with_special_characters_works():
    """Test that repeated_word works on string with special characters
    """
    text = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    actual = repeated_word(text)
    expected = 'summer'
    assert actual == expected


def test_returns_false_with_no_repeated_words():
    """Test that repeated_word returns False when there are no special characters
    """
    text = 'all these words are different'
    actual = repeated_word(text)
    assert actual is False


def test_returns_false_with_blank_string():
    """Test that repeated_word returns False when passed an empty string
    """
    text = ''
    actual = repeated_word(text)
    assert actual is False


def test_raises_exception_with_numeric_entry():
    """Test get method returns error message when given non-string key
    """
    with pytest.raises(Exception):
        repeated_word(98712213)
