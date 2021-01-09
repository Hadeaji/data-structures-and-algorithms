from data_structures_and_algorithms.data_structures.hashtable.hashtable import *
import pytest                                       

# Adding a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored

def test_adding_ht(hashtab):
    assert hashtab.map[hashtab.hash('name')].head.value == 'Hadi'
    hashtab.add('color','black as my future')
    assert hashtab.map[hashtab.hash('color')].head.value == 'black as my future'

def test_contain_ht(hashtab):
    assert hashtab.contains('name') == True
    assert hashtab.contains('room') == False

def test_collision_ht(hashtab):
    assert hashtab.map[hashtab.hash('coldu')].head.value == 344
    assert hashtab.map[hashtab.hash('cloud')].head.next.value == 34
    assert hashtab.map[hashtab.hash('could')].head.next.next.value == 67

    assert hashtab.get('cloud') == 34

@pytest.fixture
def hashtab():
    test = Hashtable(1024)
    test.add('name', 'Hadi')
    test.add('could', 67)
    test.add('cloud', 34)
    test.add('coldu', 344)
    return test
