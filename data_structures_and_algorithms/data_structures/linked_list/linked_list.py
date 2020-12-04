class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    """
    This class creates new Linked List and append items to it using insert method
    that accepts 1 Argument, Can search for 1 Argument at a time in the Linked Lust created,
    And can retrn a string of the linked list
    """
    
    def __init__(self):
        self.head = None

    def insert(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self,value):
        if self.head != None:
            current = self.head
            while current:
                if current.value == value:
                    return True
                else:
                    current = current.next
            return False
        else:
            return False

    def __str__(self):
        result= ''
        current = self.head
        while current:
            result += f'{{{current.value}}}->'
            current = current.next
            if current == None:
                result += 'NULL'
        
        return result

if __name__ == "__main__":
    ll=LinkedList()
    ll.insert(9)
    ll.insert(4)
    print(ll.includes(9))
