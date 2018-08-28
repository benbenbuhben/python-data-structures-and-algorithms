from .queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    queue = Wueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    return queue


def test_queue_class_exists():
    assert queue


def test_can_instantiate_empty_queue(empty_queue):
    assert isinstance(empty_queue, Wueue)


def test_insertion_of_value_increases_length(empty_queue):
    assert len(empty_queue) == 0
    empty_queue.push(100)
    assert len(empty_queue) == 1


def test_default_value_of_top(empty_queue):
    assert empty_queue.top is None


