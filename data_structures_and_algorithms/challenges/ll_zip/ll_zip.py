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

    i =0
    j =0
    current1 = ll1.head
    current2 = ll2.head

    while current1:
        i += 1
        current1 = current1.next
        if current1 == None:
            break 
    while current2:
        j += 1
        current2 = current2.next
        if current2 == None:
            break 

    if j <= i:
        current1 = ll1.head
        current2 = ll2.head

    if i < j:
        head = ll2.head.value
        current1 = ll2.head
        current2 = ll1.head


    while current1 != None or current2 != None:

        if current2 != None:
            temp = current1.next
            temp2 = current2.next
            current1.next = current2
            current1 = current1.next
            if temp != None:
                current1.next = temp
                current1 = current1.next
            current2 = temp2
        

        if current1.next == None and current2 == None:
            current1 = current1.next

        if current1 == None:
            if i < j:
                ll1.insert(head)
            return ll1

if __name__ == "__main__":
    ll1=LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(2)

    print(ll1)

    ll2=LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(4)
    ll2.append(8)

    print(ll2)

    print(zipLists(ll1,ll2))