from data_structures_and_algorithms.challenges.merge_sort.merge_sort import *
import pytest

def test_merge_sort_1(fixed_array1):  
    merge_sort(fixed_array1)
    assert fixed_array1 == [-2, 5, 8, 12, 18, 20]

def test_merge_sort_2(fixed_array2):  
    merge_sort(fixed_array2)
    assert fixed_array2 == [5, 5, 5, 7, 7, 12]

def test_merge_sort_3(fixed_array3):  
    merge_sort(fixed_array3)
    assert fixed_array3 == [2, 3, 5, 7, 11, 13]

@pytest.fixture
def fixed_array1():
    bt = [20,18,12,8,5,-2]
    return bt

@pytest.fixture
def fixed_array2():
    bt = [5,12,7,5,5,7]
    return bt

@pytest.fixture
def fixed_array3():
    bt = [2,3,5,7,13,11]
    return bt