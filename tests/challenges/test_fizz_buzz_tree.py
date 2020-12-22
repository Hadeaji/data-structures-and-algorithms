from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import *
import pytest

def test_FizzBuzzTree_1(fixed_tree_with_elements):  
    assert FizzBuzzTree(fixed_tree_with_elements).breadth_first() == ['4', '-1', 'Fizz', 'Fizz', '8', 'Fizz', 'FizzBuzz']

def test_FizzBuzzTree_2():
    tree = BinaryTree()
    assert FizzBuzzTree(tree).breadth_first() == ['Tree is Empty']


@pytest.fixture
def fixed_tree_with_elements():
    bt = BinaryTree()
    bt.root = Node(4)
    bt.root.right = Node(9)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(15)
    bt.root.left.left = Node(3)
    bt.root.left.right = Node(8)
    return bt