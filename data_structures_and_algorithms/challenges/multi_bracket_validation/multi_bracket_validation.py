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

#####################################################

def multi_bracket_validation(string):
    stack1 = Stack()

    values = [char for char in string]
    for i in values:
        if i == '{' or i == '[' or i == '(':
            stack1.push(i)
        else:
            if i == '}' or i == ']' or i == ')':
                x=0
                if i == '}':
                    x = '{'
                if i == ']':
                    x = '['
                if i == ')':
                    x = '('

                if x == stack1.peek():
                    stack1.pop()
                else:
                    return False

    if stack1.top != None:
        return False
    else:
        return True
