class HashNode:
    """
    Noder till klassen Hashtable 
    """

    def __init__(self, key = "", data = None, pointer = None):
        """key är nyckeln som anvands vid hashningen
            data är det objekt som ska hashas in"""
        self.key = key
        self.data = data
        self.pointer = pointer #pointer, points on child

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size #can be used to tell how many objects in table
        self.table = [None] * size #creates a table with capacity number of elements and all elements are set to None
        self.collisions = 0


    def store(self, key, data):
        """ 
        key är nyckeln
        data är objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen.
        """    
        index = self.hashfunction(key) 
        print(index)
        if self.table[index] is None: 
            self.table[index] = HashNode(key, data)
        else:
            """
            Lägger in den nya saken längst fram och flyttar bak de gamla sakerna
            så det som las in först kommer ligga "längst bak" i linked list
            """
            self.collisions += 1
            existing_node = self.table[index]
            self.table[index] = HashNode(key, data)
            self.table[index].pointer = existing_node
        
    def search(self, key):
        """key är nyckeln
            Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
            Om "key" inte finns ska det bli KeyError """
        #Fyll i kod här!
        index = self.hashfunction(key) 
        node = self.table[index]
        while node is not None:
            if node.key is key:
                return node
            node = node.pointer
        raise KeyError

    def hashfunction(self, key):
        """key är nyckeln
            Beräknar hashfunktionen för key"""
        #Fyll i kod här!
        hash_num = ""
        for i in key[::-1]:
            hash_num += str(len(key)*1117 + ord(i)**2)

        print(hash_num)
        return int(hash_num) % self.size #returnerar index

#size = kdrama.size  * 2  (skapa en dubbelt så stor tabell som draman)
# obj_hash = Hashtable()
# obj_hash.store(key, value)

def main():
    hashtable = None
    
    while True:
        line = input()
        key, *value = line.split()
        if key == '#':
            print('#')
            break
        elif key == 'init' and len(value) > 0:
            size = int(value[0])
            hashtable = Hashtable(size)
            print('New size:', size)
        elif len(value) > 0:
            hashtable.store(key, value[0])
            print(key, '<-', value[0])
        else:
            try:
                value = hashtable.search(key)
                print(f'{key}: {value}')
            except KeyError:
                print('KeyError:', key)


if __name__ == "__main__":
    main()
