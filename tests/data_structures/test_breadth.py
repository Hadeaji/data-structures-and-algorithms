from data_structures_and_algorithms.data_structures.tree.tree import Node,BinarySearchTree,BinaryTree
import pytest

def test_breadth_1(fixed_tree_with_elements):  
    assert fixed_tree_with_elements.breadth_first() == [7, 5, 9, 1, 8, 11]

def test_breadth_2(fixed_tree_with_elements_2):  
    assert fixed_tree_with_elements_2.breadth_first() == [23, 43, 34, 67, 56, 89]

def test_breadth_3():
    tree=BinarySearchTree()
    assert tree.breadth_first() == 'Empty Tree'

@pytest.fixture
def fixed_tree_with_elements():
    tree=BinarySearchTree()
    tree.add(7)
    tree.add(9)
    tree.add(5)
    tree.add(11)
    tree.add(8)
    tree.add(1)
    return tree

@pytest.fixture
def fixed_tree_with_elements_2():
    tree=BinarySearchTree()
    tree.add(23)
    tree.add(43)
    tree.add(34)
    tree.add(67)
    tree.add(56)
    tree.add(89)
    return tree