import pytest
from random import shuffle
from sorting_algos.merge_sort.merge import merge_sort


def test_merge_sort_module_exists():
    return merge_sort


def test_small_shuffled_list_gets_sorted():
    expected = [num for num in range(20)]
    arr = expected[:]
    shuffle(arr)
    merge_sort(arr, 0, len(arr)-1)
    assert expected == arr


def test_big_shuffled_list_gets_sorted():
    expected = [num for num in range(1000)]
    arr = expected[:]
    shuffle(arr)
    merge_sort(arr, 0, len(arr)-1)
    assert expected == arr


def test_sorts_already_sorted():
    expected = [num for num in range(20)]
    temp = expected
    merge_sort(expected, 0, len(expected)-1)
    assert expected == temp


def test_sorts_list_of_duplicates():
    arr = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    merge_sort(arr, 0, len(arr)-1)
    assert expected == arr


def test_sort_validates_expected_input():
    with pytest.raises(TypeError):
        merge_sort('wuddup world')
