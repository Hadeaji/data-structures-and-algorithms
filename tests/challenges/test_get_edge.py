from data_structures_and_algorithms.challenges.get_edge.get_edge import *
import pytest


def test_get_edge_1(graph_test):
    actual = get_edge(graph_test,['Metroville', 'Pandora',])
    expect = 'True, $82'
    assert expect == actual

def test_get_edge_2(graph_test):
    actual = get_edge(graph_test,['Arendelle', 'New Monstropolis', 'Naboo'])
    expect = 'True, $115'
    assert expect == actual

def test_get_edge_3(graph_test):
    actual = get_edge(graph_test,['Naboo','Pandora'])
    expect = False
    assert expect == actual

def test_get_edge_4(graph_test):
    actual = get_edge(graph_test,['Narnia', 'Arendelle', 'Naboo'])
    expect = False
    assert expect == actual


@pytest.fixture
def graph_test():
    test1 = Graph()
    test1.add_node('Metroville')
    test1.add_node('Pandora')
    test1.add_node('Arendelle')
    test1.add_node('New Monstropolis')
    test1.add_node('Naboo')
    test1.add_node('Narnia')

    test1.add_edge('Pandora','Arendelle',150)
    test1.add_edge('Pandora','Metroville',82)

    test1.add_edge('Metroville','Pandora',82)
    test1.add_edge('Metroville','Arendelle',99)
    test1.add_edge('Metroville','New Monstropolis',105)
    test1.add_edge('Metroville','Naboo',26)
    test1.add_edge('Metroville','Narnia',37)

    test1.add_edge('Arendelle','New Monstropolis',42)
    test1.add_edge('Arendelle','Metroville',99)
    test1.add_edge('Arendelle','Pandora',150)

    test1.add_edge('New Monstropolis','Arendelle',42)
    test1.add_edge('New Monstropolis','Metroville',105)
    test1.add_edge('New Monstropolis','Naboo',73)

    test1.add_edge('Naboo','New Monstropolis',73)
    test1.add_edge('Naboo','Metroville',26)
    test1.add_edge('Naboo','Narnia',250)

    test1.add_edge('Narnia','Metroville',37)
    test1.add_edge('Narnia','Naboo',250)

    return test1