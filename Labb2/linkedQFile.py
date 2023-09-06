
class Node(): #element of linked list
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

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
        if self.isEmpty(): #ifall linked lsitan är tom
            self._first= new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
    
    def dequeue(self): #vill ta bort första saken i kön
        item_to_retrieve = self._first #sparar värde av försa saken i kön
        self._first = self._first.next # gör att första saken i listan blir saken som låg efter first
        return item_to_retrieve.value
        
    
    def isEmpty(self):
        if self._first is None:
            return True
        else:
            return False
        
