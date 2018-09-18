import pytest
from .graph import Graph
import io
import sys
from contextlib import contextmanager


@pytest.fixture()
def empty_graph():
    g = Graph()
    return g


@pytest.fixture()
def filled_graph():
    g = Graph()
    g.add_vert('A')
    g.add_vert('B')
    g.add_vert('C')
    g.add_vert('D')
    g.add_vert('E')
    g.add_vert('F')
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('C', 'E')
    g.add_edge('C', 'F')
    g.add_edge('D', 'F')
    g.add_edge('E', 'F')
    return g


@pytest.fixture()
def filled_weighted_graph():
    g = Graph()
    g.add_vert('A')
    g.add_vert('B')
    g.add_vert('C')
    g.add_vert('D')
    g.add_vert('E')
    g.add_vert('F')
    g.add_edge('A', 'B', 5)
    g.add_edge('B', 'C', 10)
    g.add_edge('B', 'D', 15)
    g.add_edge('C', 'D', 20)
    g.add_edge('C', 'E', 25)
    g.add_edge('C', 'F', 30)
    g.add_edge('D', 'F', 35)
    g.add_edge('E', 'F', 40)
    return g

@contextmanager
def captured_output():
    '''Helper function for testing stdout
    '''
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def test_graph_exists():
    """Test graph module linked in correctly.
    """
    assert Graph


def test_graph_adds_edge(filled_graph):
    """Test graph adds edge
    """
    filled_graph.add_edge('F', 'A')
    assert filled_graph.graph == {'A': ['B'], 'B': ['C', 'D'], 'C': ['D', 'E', 'F'], 'D': ['F'], 'E': ['F'], 'F': ['A']}


def test_graph_adds_vert(filled_graph):
    """Test graph add vertex method works
    """
    filled_graph.add_vert('G')
    assert filled_graph.graph == {'A': ['B'], 'B': ['C', 'D'], 'C': ['D', 'E', 'F'], 'D': ['F'], 'E': ['F'], 'F': [], 'G': []}


def test_has_vert(filled_graph):
    assert filled_graph.has_vert('D')


def test_doesnt_have_vert(filled_graph):
    assert not filled_graph.has_vert('Q')


def test_gets_neighbors_raises_error(filled_graph):
    try:
        filled_graph.get_neighbors('Z')
        assert False
    except KeyError:
        assert True


def test_gets_neighbors_returns_neighbors(filled_graph):
    assert filled_graph.get_neighbors('C') == ['D', 'E', 'F']


def test_returns_length(filled_graph):
    assert len(filled_graph) == 6


def test_returns_length_empty(empty_graph):
    assert len(empty_graph) == 0


def test_breadth_first_works(filled_graph):
    with captured_output() as (out, err):
        print(filled_graph.breadth_first('A'))
    output = out.getvalue().strip()
    assert output == 'A\nB\nC\nD\nE\nF\nNone'
