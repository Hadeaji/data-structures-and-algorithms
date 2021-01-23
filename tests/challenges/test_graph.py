from data_structures_and_algorithms.data_structures.graph.graph import *
import pytest


def test_graph_props_1(graph_test):

    actual = graph_test.get_neighbours('a')
    expect = [[4,'b'],[9,'d'],[3,'c']]
    assert expect == actual

def test_graph_props_2(graph_test):

    actual = graph_test.size()
    expect = 4
    assert actual == expect

    
def test_custom_graph():
    test2 = Graph()
    test2.add_node('a')
    assert test2.get_neighbours('a') == []
    assert test2.size() == 1
    assert test2.get_neighbours('x') == 'Node does not exist'


@pytest.fixture
def graph_test():
    test1 = Graph()
    test1.add_node('a')
    test1.add_node('b')
    test1.add_node('c')
    test1.add_node('d')
    test1.add_edge('a','b',4)
    test1.add_edge('a','d',9)
    test1.add_edge('a','c',3)
    test1.add_edge('b','a',4)
    test1.add_edge('c','a',3)
    test1.add_edge('c','d',6)
    test1.add_edge('d','a',9)
    test1.add_edge('d','b',5)
    test1.add_edge('d','c',6)
    return test1