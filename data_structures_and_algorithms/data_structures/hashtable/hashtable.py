class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    """
    This class creates new Linked List and append items to it using insert method
    that accepts 1 Argument And can retrn a string of the linked list
    """

    def __init__(self):
        self.head = None

    def insert(self,key,value):
        new_node = Node(key,value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        result= ''
        current = self.head
        while current:
            result += f'{{{current.key}}}: {{{current.value}}}->'
            current = current.next
            if current == None:
                result += 'NULL'
        return result

class Hashtable:
    def __init__(self,size):
        self.size = size
        self.map = [None]*size

    def add(self,key,value):
        room = self.hash(key)

        if self.map[room] == None:
            self.map[room] = LinkedList()
            self.map[room].insert(key,value)    
        else:
            self.map[room].insert(key,value)

    def get(self,key):
        room = self.hash(key)

        if self.map[room] == None:
            return self.map[room]
        else:
            current = self.map[room].head
            while current:
                if current.key == key:
                    return current.value
                current = current.next

    def contains(self,key):
        room = self.hash(key)
        if self.map[room] != None:
            return True
        else:
            return False

    def hash(self,key):
        pointer = 0
        for char in key:
            pointer += ord(char)
        pointer *= 199
        pointer %= self.size
        return pointer