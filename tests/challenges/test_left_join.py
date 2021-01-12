from data_structures_and_algorithms.challenges.left_join.left_join import *
import pytest

def test_left_join_1(hashyt1,hashyt2):  
    assert left_join(hashyt1,hashyt2) == [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outift', 'garb', None], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight']]

def test_left_join_2(hashyt1,hashyt3):  
    assert left_join(hashyt1,hashyt3) == [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outift', 'garb', None], ['diligent', 'employed', None], ['wrath', 'anger', None]]

def test_left_join_3(hashyt4,hashyt3):
    assert left_join(hashyt4,hashyt3) == [['flow', 'jam', None]]

@pytest.fixture
def hashyt1():
    test = Hashtable(1024)
    test.add('fond', 'enamored')
    test.add('wrath', 'anger')
    test.add('diligent', 'employed')
    test.add('outift', 'garb')
    test.add('guide', 'usher')

    return test

@pytest.fixture
def hashyt2():
    test2 = Hashtable(1024)
    test2.add('fond', 'averse')
    test2.add('wrath', 'delight')
    test2.add('diligent', 'idle')
    test2.add('guide', 'follow')
    test2.add('flow', 'jam')

    return test2

@pytest.fixture
def hashyt3():
    test2 = Hashtable(1024)
    test2.add('fond', 'averse')
    test2.add('guide', 'follow')

    return test2

@pytest.fixture
def hashyt4():
    test2 = Hashtable(1024)
    test2.add('flow', 'jam')

    return test2
