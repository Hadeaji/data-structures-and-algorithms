class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preOrder(self):
        output=[]

        def _walk(node):
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output

    def inOrder(self):
        output=[]

        def _walk(node):
            if node.left:
                _walk(node.left)
            output.append(node.value)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output
    

    def postOrder(self):
        output=[]

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output.append(node.value)

        _walk(self.root)
        return output


class BinarySearchTree(BinaryTree):

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            def _walk(node):

                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        _walk(node.left)
                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        _walk(node.right)
                        
            _walk(self.root)

    def contains(self,value):
        if self.root:
            current = self.root
            def _walk(current):
                if value == current.value:
                    return True
                elif value < current.value:
                    current = current.left
                    if current:
                        return _walk(current)
                elif value > current.value:
                    current = current.right
                    if current:
                        return _walk(current)

            if _walk(current) == True:
                return True
            else:
                return False
        else:
            return False
