from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)

import pytest

def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)

def test_insert(fixed_list):
    assert fixed_list.head.value == 4
    assert fixed_list.head.next.value  == 9

def test_includes(fixed_list):
    assert fixed_list.includes(9) == True
    assert fixed_list.includes(7) == False

def test_ll_values(fixed_list):
    assert str(fixed_list) == f'{{4}}->{{9}}->NULL'

@pytest.fixture
def fixed_list():
        ll=LinkedList()
        ll.insert(9)
        ll.insert(4)
        return ll