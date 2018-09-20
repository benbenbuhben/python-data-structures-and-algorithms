import pytest
from data_structures.graph.graph import Graph
from challenges.graph.get_edges.get_edges import get_edges


@pytest.fixture()
def filled_weighted_graph():
    """Pytest fixture exactly like the example in the assignment
    """
    g = Graph()
    g.add_vert('Pandora')
    g.add_vert('Arendelle')
    g.add_vert('Metroville')
    g.add_vert('Monstropolis')
    g.add_vert('Narnia')
    g.add_vert('Naboo')
    g.add_edge_directed('Pandora', 'Arendelle', 150)
    g.add_edge_directed('Pandora', 'Metroville', 82)
    g.add_edge_directed('Arendelle', 'Metroville', 99)
    g.add_edge_directed('Arendelle', 'Monstropolis', 42)
    g.add_edge_directed('Metroville', 'Monstropolis', 105)
    g.add_edge_directed('Monstropolis', 'Naboo', 73)
    g.add_edge_directed('Metroville', 'Narnia', 37)
    g.add_edge_directed('Metroville', 'Naboo', 26)
    g.add_edge_directed('Narnia', 'Naboo', 250)
    return g


def test_returns_false_when_given_cities_that_do_not_exist(filled_weighted_graph):
    """get_edges() returns false when given an itinerary including cities that are airline does not service
    """
    itinerary = ['Seattle', 'New York City']
    actual = get_edges(filled_weighted_graph, itinerary)
    assert not actual


def test_get_edge_returns_false_when_no_direct_flights_case1(filled_weighted_graph):
    """get_edges() returns false when there are no direct flights between two of the cities in the itinerary
    """
    itinerary = ['Naboo', 'Pandora']
    actual = get_edges(filled_weighted_graph, itinerary)
    assert not actual


def test_get_edge_returns_false_when_no_direct_flights_case2(filled_weighted_graph):
    """get_edges() returns false when there are no direct flights between two of the cities in the itinerary
    """
    itinerary = ['Narnia', 'Arendelle', 'Naboo']
    actual = get_edges(filled_weighted_graph, itinerary)
    assert not actual


def test_get_edge_returns_cost_when_direct_flights_available_case1(filled_weighted_graph):
    """get_edges() returns the total cost when there are direct flights available between all the cities in the itinerary
    """
    itinerary = ['Arendelle', 'Monstropolis', 'Naboo']
    actual = get_edges(filled_weighted_graph, itinerary)
    assert actual == 115


def test_get_edge_returns_cost_when_direct_flights_available_case2(filled_weighted_graph):
    """get_edges() returns the total cost when there are direct flights available between all the cities in the itinerary
    """
    itinerary = ['Metroville', 'Pandora']
    actual = get_edges(filled_weighted_graph, itinerary)
    assert actual == 82


