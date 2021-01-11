class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
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
    
    def find_maximum_value(self):
        self.max=self.root.value

        def _walk(node):
            if node.value > self.max:
                self.max =node.value
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return self.max

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

def tree_intersection(tree1,tree2):
    if (tree1.root == None):
        return 'Tree 1 is empty'
    elif (tree2.root == None):
        return 'Tree 2 is empty'
    else:
        ar1 = tree1.preOrder()
        ar2 = set(tree2.preOrder())
        temp = []
        for i in ar1:
            if i in ar2:
                temp.append(i)
        if len(temp) != 0:
            return temp
        else:
            return 'No Common Values'


if __name__ == "__main__":
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

    print(tree_intersection(bt,bt2))
