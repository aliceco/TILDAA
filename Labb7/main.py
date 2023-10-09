class HashNode:
    """
    Noder till klassen Hashtable 
    """

    def __init__(self, key = "", data = None):
        """key är nyckeln som anvands vid hashningen
            data är det objekt som ska hashas in"""
        self.key = key
        self.data = data

#Fyll i kod här nedan för att initiera hashtabellen

class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size

    def store(self, key, data):
        """key är nyckeln
            data är objektet som ska lagras
            Stoppar in "data" med nyckeln "key" i tabellen."""
        index = self.key 
        

    def search(self, key):
        """key är nyckeln
            Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
            Om "key" inte finns ska det bli KeyError """
        #Fyll i kod här!
        #...
        else:
            raise KeyError

    def hashfunction(self, key):
        """key är nyckeln
            Beräknar hashfunktionen för key"""
        #Fyll i kod här!

        return key
