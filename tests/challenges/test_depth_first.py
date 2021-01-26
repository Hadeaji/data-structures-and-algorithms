from data_structures_and_algorithms.challenges.depth_first.depth_first import *
import pytest

def test_depth_first_graph_1(graph_test):
    actual = DFS(graph_test)
    expect = ['a', 'c', 'd', 'b']
    assert expect == actual

@pytest.fixture
def graph_test():
    test1 = Graph()
    test1.add_node('a')
    test1.add_node('b')
    test1.add_node('c')
    test1.add_node('d')
    test1.add_node('x')
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