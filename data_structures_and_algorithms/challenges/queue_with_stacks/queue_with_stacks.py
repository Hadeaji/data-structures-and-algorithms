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

class PseudoQueue:
    def __init__(self): 
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self,value):
        self.s1.push(value)

    def dequeue(self):
        if not self.s2.top:
            if not self.s1.top:
                return "Can't dequeue from empty queue!"
        
            while self.s1.top:
                s1_top = self.s1.pop()
                self.s2.push(s1_top)

            result = self.s2.pop()
            temp = self.s2
            self.s2 = Stack()

            while temp.top:
                temp_top = temp.pop()
                self.s1.push(temp_top)

            return result
        


if __name__ == "__main__":
    kk = PseudoQueue()
    kk.enqueue(4)
    kk.enqueue(5)
    kk.enqueue(6)
    print(kk.enqueue(7))
    print(kk.dequeue())