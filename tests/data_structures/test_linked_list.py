from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)

import pytest

def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)

def test_insert(fixed_list):
    assert fixed_list.head.value == 3
    assert fixed_list.head.next.value  == 4

def test_includes(fixed_list):
    assert fixed_list.includes(9) == True
    assert fixed_list.includes(7) == False

def test_ll_values(fixed_list):
    assert str(fixed_list) == f'{{3}}->{{4}}->{{9}}->NULL'

# Can successfully add a node to the end of the linked list
def test_ll_append(fixed_list):
    fixed_list.append(0)
    assert str(fixed_list) == f'{{3}}->{{4}}->{{9}}->{{0}}->NULL'

# Can successfully add multiple nodes to the end of a linked list
def test_ll_multiple_append(fixed_list):
    fixed_list.append(5)
    fixed_list.append(1)
    fixed_list.append(7)
    assert str(fixed_list) == f'{{3}}->{{4}}->{{9}}->{{5}}->{{1}}->{{7}}->NULL'

# Can successfully insert a node before a node located i the middle of a linked list

def test_ll_insert_before(fixed_list):
    fixed_list.insertBefore(4,1)
    assert str(fixed_list) == f'{{3}}->{{1}}->{{4}}->{{9}}->NULL'

# Can successfully insert a node before the first node of a linked list

def test_ll_insert_before_first(fixed_list):
    fixed_list.insertBefore(3,1)
    assert str(fixed_list) == f'{{1}}->{{3}}->{{4}}->{{9}}->NULL'

# Can successfully insert after a node in the middle of the linked list

def test_ll_insert_after(fixed_list):
    fixed_list.insertAfter(4,1)
    assert str(fixed_list) == f'{{3}}->{{4}}->{{1}}->{{9}}->NULL'

# Can successfully insert a node after the last node of the linked list

def test_ll_insert_after_last(fixed_list):
    fixed_list.insertAfter(9,1)
    assert str(fixed_list) == f'{{3}}->{{4}}->{{9}}->{{1}}->NULL'



# Where k is greater than the length of the linked list

def test_ll_greater_than_the_length(fixed_list):
    assert fixed_list.kthFromEnd(9) == f'Sorry Your Input Is Out Of Range'

# Where k and the length of the list are the same

def test_ll_length_of_same(fixed_list):
    assert fixed_list.kthFromEnd(3) == f'Sorry Your Input Is Out Of Range'

# Where k is not a positive integer

def test_ll_not_a_positive(fixed_list):
    assert fixed_list.kthFromEnd(-3) == 'Sorry Do Not Accept Negative Values'

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

def test_ll_kthFromEnd_1(fixed_list):
    assert fixed_list.kthFromEnd(2) == 3

def test_ll_kthFromEnd_2(fixed_list):
    assert fixed_list.kthFromEnd(0) == 9



@pytest.fixture
def fixed_list():
        ll=LinkedList()
        ll.insert(9)
        ll.insert(4)
        ll.insert(3)
        return ll