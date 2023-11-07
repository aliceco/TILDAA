
class Node(): #element of linked list
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQ():
    def __init__(self):
        self._first = None
        self._last = None
    
    def __str__(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            resultat = []
            element = self._first
            while element is not None:
                resultat.append(str(element.value))
                element = self._first.next
        return resultat

    def enqueue(self,x):
        new_node = Node(x)
        if self.isEmpty(): #ifall linked kön är tom
            self._first= new_node #head "pekar" på första noden
            self._last = new_node #tail "pekar" på första noden då det bara är den noden som ligger i kön
        else:
            self._last.next = new_node #den nya noden läggs till efter första noden
            self._last = new_node #den nya noden är den sista noden i kön
    
    def dequeue(self): #vill ta bort första saken i kön
        item_to_retrieve = self._first #sparar noden av försa saken i kön
        self._first = self._first.next # gör att första noden i listan blir noden som låg efter vad som förut va första noden
        return item_to_retrieve.value
        
    def isEmpty(self):
        if self._first is None:
            return True
        else:
            return False
        
    def peek(self):
        if self.isEmpty() is True:
            return None
        else:
            return self._first.value
        

        
