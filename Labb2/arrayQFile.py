from array import array

class ArrayQ:

    def __init__(self):
        self._arr = array('i') #gör attributen array privat, bestämmer typen som matas in 

    def __str__(self):
        return str(self._arr)
    
    def enqueue(self,x):
        self._arr.append(x)
    
    def dequeue(self):
        return self._arr.pop(0)
    
    
def maain():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")


if __name__ == "__main__": # fattar inte vad den här ska göra? den fungerar inte
    maain()