from data_structures_and_algorithms.data_structures.tree.tree import Node,BinarySearchTree,BinaryTree
import pytest

# Can successfully instantiate an empty tree
def test_empty_tree():  
    new_tree = BinarySearchTree()
    assert new_tree.root == None

# Can successfully instantiate a tree with a single root node
def test_single_root_node(fixed_tree):
    fixed_tree.add(9)
    assert fixed_tree.root.value == 9

# Can successfully add a left child and right child to a single root node
def test_left_right_node(fixed_tree):  
    fixed_tree.add(9)
    fixed_tree.add(5)
    fixed_tree.add(10)
    assert fixed_tree.root.left.value == 5
    assert fixed_tree.root.right.value == 10

# Can successfully return a collection from a preorder traversal
def test_preOrder(fixed_tree_with_elements):  
    assert fixed_tree_with_elements.preOrder() == [7, 5, 1, 9, 8, 11]

# Can successfully return a collection from an inorder traversal
def test_inOrder(fixed_tree_with_elements):  
    assert fixed_tree_with_elements.inOrder() == [1, 5, 7, 8, 9, 11]

# Can successfully return a collection from a postorder traversal
def test_postOrder(fixed_tree_with_elements):  
    assert fixed_tree_with_elements.postOrder() == [1, 5, 8, 11, 9, 7]


@pytest.fixture
def fixed_tree():
    tree=BinarySearchTree()
    return tree

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