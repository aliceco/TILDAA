class HashNode:
    """
    Noder till klassen Hashtable 
    """

    def __init__(self, key = "", data = None, pointer = None):
        self.key = key
        self.data = data
        self.pointer = pointer #pointer, points on child

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:

    def __init__(self, size):
        self.size = size #can be used to tell how many objects in table
        self.table = [None] * size #creates a table with capacity number of elements and all elements are set to None
        self.collisions = 0


    def store(self, key, data):
        index = self.hashfunction(key) 
        if self.table[index] is None: 
            self.table[index] = HashNode(key, data)
        else:
            self.collisions += 1
            existing_node = self.table[index]
            self.table[index] = HashNode(key, data)
            self.table[index].pointer = existing_node
        
    def search(self, key):
        index = self.hashfunction(key) #calculates index of the input
        element = self.table[index] #saves whats on that index into a variable 
        while element is not None: #checks if it's empty
            if element.key == key: #if the key of the element is the same as the ipnut key
                return element.data #return the data of the element
            element = element.pointer #otherwise check the next 

        raise KeyError

    def hashfunction(self, key):
        hash_num = ""
        for i in key[::-1]:
            hash_num += str(len(key)*27 + ord(i)**2)
        return int(hash_num) % self.size #returnerar index
