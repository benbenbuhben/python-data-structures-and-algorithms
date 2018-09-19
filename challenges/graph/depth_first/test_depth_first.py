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
    g.add_edge_undirected('A', 'B')
    g.add_edge_undirected('A', 'D')
    g.add_edge_undirected('B', 'C')
    g.add_edge_undirected('B', 'D')
    g.add_edge_undirected('C', 'G')
    g.add_edge_undirected('D', 'E')
    g.add_edge_undirected('D', 'F')
    g.add_edge_undirected('D', 'H')
    g.add_edge_undirected('F', 'H')
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


def test_ll_merge_zips_two_empty_lists(empty_list1, empty_list2):
    actual = depth_first(filled_graph, 'A')
    with captured_output() as (out, err):
        print(actual)
    output = out.getvalue().strip()
    assert output == '(Head: None)'
