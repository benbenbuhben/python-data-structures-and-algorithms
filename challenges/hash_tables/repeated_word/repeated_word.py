from data_structures.hash_table.hash_table import HashTable
import re


def repeated_word(text):
    """Function that takes in text as input and returns the first repeated word if there is one. Otherwise, returns False.
    """
    h = HashTable()
    cleaned_text = re.sub('\W+', ' ', text)
    words = cleaned_text.split()
    for word in words:
        result = h._set(word.lower())
        if result == 'Updated Value':
            return word
    return False
