import pytest
from random import shuffle
from sorting_algos.selection_sort.selection import selection_sort


def test_selection_sort_module_exists():
    return selection_sort


def test_small_shuffled_list_gets_sorted():
    expected = [num for num in range(20)]
    unsorted = expected[:]
    shuffle(unsorted)
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_big_shuffled_list_gets_sorted():
    expected = [num for num in range(1000)]
    unsorted = expected[:]
    shuffle(unsorted)
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_sorts_already_sorted():
    expected = [num for num in range(20)]
    now_sorted = selection_sort(expected)
    assert expected == now_sorted


def test_sorts_list_of_duplicates():
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = selection_sort(unsorted)
    assert expected == now_sorted


def test_sort_validates_expected_input():
    with pytest.raises(TypeError):
        selection_sort('wuddup world')
