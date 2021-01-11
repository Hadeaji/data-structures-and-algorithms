from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import *
import pytest

def test_tree_intersection_1(tree1,tree2):  
    assert tree_intersection(tree1,tree2) == [100, 160, 125, 175, 200, 350, 500]

def test_tree_intersection_2(tree1,tree3):  
    assert tree_intersection(tree1,tree3) == 'Tree 2 is empty'

def test_tree_intersection_3(tree1,tree4):
    assert tree_intersection(tree1,tree4) == 'No Common Values'


@pytest.fixture
def tree1():
    bt = BinaryTree()
    bt.root = Node(150)
    bt.root.right = Node(250)
    bt.root.left = Node(100)

    bt.root.right.left = Node(200)
    bt.root.right.right = Node(350)

    bt.root.right.right.right = Node(500)
    bt.root.right.right.left = Node(300)

    bt.root.left.left = Node(75)
    bt.root.left.right = Node(160)

    bt.root.left.right.right = Node(175)
    bt.root.left.right.left = Node(125)
    return bt

@pytest.fixture
def tree2():
    bt2 = BinaryTree()
    bt2.root = Node(42)
    bt2.root.right = Node(600)
    bt2.root.left = Node(100)

    bt2.root.right.left = Node(200)
    bt2.root.right.right = Node(350)

    bt2.root.right.right.right = Node(500)
    bt2.root.right.right.left = Node(4)

    bt2.root.left.left = Node(15)
    bt2.root.left.right = Node(160)

    bt2.root.left.right.right = Node(175)
    bt2.root.left.right.left = Node(125)
    return bt2

@pytest.fixture
def tree3():
    bt3 = BinaryTree()
    return bt3

@pytest.fixture
def tree4():
    bt4 = BinaryTree()
    bt4.root = Node(1000)
    bt4.root.right = Node(1200)

    return bt4