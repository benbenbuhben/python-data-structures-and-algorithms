import pytest
from data_structures.graph.graph import Graph
from challenges.graph.depth_first.depth_first import depth_first
import io
import sys
from contextlib import contextmanager


@pytest.fixture()
def filled_graph():
    """Pytest fixture exactly like the example in the assignment
    """
    g = Graph()
    g.add_vert('A')
    g.add_vert('B')
    g.add_vert('C')
    g.add_vert('D')
    g.add_vert('E')
    g.add_vert('F')
    g.add_vert('G')
    g.add_vert('H')
    g.add_edge_directed('A', 'B')
    g.add_edge_directed('A', 'D')
    g.add_edge_directed('B', 'C')
    g.add_edge_directed('B', 'D')
    g.add_edge_directed('C', 'G')
    g.add_edge_directed('D', 'E')
    g.add_edge_directed('D', 'F')
    g.add_edge_directed('D', 'H')
    g.add_edge_directed('H', 'F')
    return g

@pytest.fixture()
def empty_graph():
    """Pytest fixture for an empty graph.
    """
    g = Graph()
    return g

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


def test_module_imported_properly():
    """Test that the depth_first() function was imported properly.
    """
    return depth_first


def test_depth_first_works(filled_graph):
    """Test that the function works on the example provided in the assignment.
    """
    with captured_output() as (out, err):
        depth_first(filled_graph, 'A')
    output = out.getvalue().strip()
    assert output == 'A\nB\nC\nG\nD\nE\nF\nH'


def test_root_not_in_graph_raises_exception(empty_graph):
    """Test that the function raises an exception when passed a root that does not exists in the graph.
    """
    with pytest.raises(Exception):
        depth_first(empty_graph, 'A')

