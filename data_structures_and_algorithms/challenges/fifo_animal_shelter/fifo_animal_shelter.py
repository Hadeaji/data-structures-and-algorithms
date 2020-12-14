class Dog:
    def __init__(self,value):
        self.value = value
        self.kind = 'Dog'
        self.next = None

class Cat:
    def __init__(self,value):
        self.value = value
        self.kind = 'Cat'
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,animal):
        new_node = animal

        if self.rear:
            self.rear.next = new_node
            self.rear = new_node

        else:
            self.front = new_node
            self.rear = new_node

    def dequeue(self,kind=None):
        if kind == None:
            if self.front:
                temp = self.front
                self.front = self.front.next
                return temp.value
        else:
            current = self.front

            if self.front.kind == kind:
                temp = self.front
                self.front = self.front.next
                return temp.value
            else:
                while current.next:
                    if current.next.kind == kind:
                        temp = current.next
                        current.next = current.next.next
                        return temp.value

                    if current.kind != kind:
                        current = current.next
                return 'NULL'

    def __str__(self):
        result= ''
        current = self.front
        while current:
            result += f'{{{current.value}}}->'
            current = current.next
            if current == None:
                result += 'NULL'
        
        return result
        

# if __name__ == "__main__":
#     shelter =AnimalShelter()
#     shelter.enqueue(Cat('ri'))
#     shelter.enqueue(Dog('jj'))
#     shelter.enqueue(Cat('roo'))
#     shelter.enqueue(Dog('jojo'))
#     print(shelter)
#     print(shelter.dequeue('Dog'))
#     print(shelter.dequeue('Bird'))
#     print(shelter.dequeue())
#     print(shelter.dequeue('Cat'))
#     print(shelter)
