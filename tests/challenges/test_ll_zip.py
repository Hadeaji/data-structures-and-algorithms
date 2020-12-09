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

    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next
            
            current.next = new_node

    def insertBefore(self,value, newVal):
        new_node = Node(newVal)

        current = self.head

        if current.value == value:
            new_node.next = current
            self.head = new_node
        else:
            while current.next:

                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
                
                if current.next == None:
                    raise Exception("Sorry Couldn't Find The Value")
                 

    def insertAfter(self,value, newVal):
        new_node = Node(newVal)

        current = self.head

        while current:

            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break

            current = current.next

            if current == None:
                raise Exception("Sorry Couldn't Find The Value")

    def kthFromEnd(self,value):
        try:
            if value < 0:
                raise Exception
        except Exception:
            return ("Sorry Do Not Accept Negative Values")
        result=[]
        current = self.head
        if current == None:
            raise Exception("Sorry Your LL Is Empty")
        while current:
            result += [current.value]
            current = current.next
            if current == None:
                break
        try:
            return result[::-1][value]
        except IndexError:
            return ("Sorry Your Input Is Out Of Range")
    
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


def zipLists(ll1,ll2):

    current1 = ll1.head
    current2 = ll2.head
    while current1 != None or current2 != None:
        
        if current2 != None:

            ll1.insertAfter(current1.value,current2.value)
            current2 = current2.next
            current1 = current1.next
        
        if current1.next != None:
            current1 = current1.next

        if current1.next == None and current2 == None:
            current1 = current1.next

        if current1 == None:
            return ll1

import pytest

#####################################################################
def test_ll_zip_1(fixed_list_1,fixed_list_2):
    fixed_list_1.append(2)
    fixed_list_2.append(4)
    assert str(zipLists(fixed_list_1,fixed_list_2)) == '{1}->{5}->{3}->{9}->{2}->{4}->NULL'

def test_ll_zip_2(fixed_list_1,fixed_list_2):
    fixed_list_2.append(4)
    assert str(zipLists(fixed_list_1,fixed_list_2)) == '{1}->{5}->{3}->{9}->{4}->NULL'

def test_ll_zip_3(fixed_list_1,fixed_list_2):
    fixed_list_1.append(2)
    assert str(zipLists(fixed_list_1,fixed_list_2)) == '{1}->{5}->{3}->{9}->{2}->NULL'

@pytest.fixture
def fixed_list_1():
    ll1=LinkedList()
    ll1.append(1)
    ll1.append(3)
    
    return ll1 

@pytest.fixture
def fixed_list_2():
    ll2=LinkedList()
    ll2.append(5)
    ll2.append(9)

    return ll2