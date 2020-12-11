class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,value):
        new_node =Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        try:
            if self.top:
                temp = self.top
                self.top = self.top.next
                return temp.value
            else:
                raise Exception('Empty Stack')
        except:
            return 'Empty Stack'

    def peek(self):
        try:
            if self.top:
                return self.top.value
            else:
                raise Exception('Empty Stack')
        except:
            return 'Empty Stack'
    
    def isEmpty(self):
        if self.top:
            return False
        elif not self.top:
            return True

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        new_node = Node(value)

        if self.rear:
            self.rear.next = new_node
            self.rear = new_node

        else:
            self.front = new_node
            self.rear = new_node

    def dequeue(self):
        try:
            if self.front:
                temp = self.front
                self.front = self.front.next
                return temp.value
            else:
                raise Exception('Empty Queue')
        except:
            return 'Empty Queue'

    def peek(self):
        try:
            if self.front:
                return self.front.value
            else:
                raise Exception('Empty Queue')
        except:
            return 'Empty Queue'

    def isEmpty(self):
        if self.front:
            return False
        elif not self.front:
            return True