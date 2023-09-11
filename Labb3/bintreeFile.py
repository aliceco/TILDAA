class Node:
    def __init__(self, value):
        self. value = value
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

def putta(p, newvalue):
    # Funktion som gör själva jobbet att stoppa in en ny nod
    #skapa nod
    #kolla om trädet är tomt 
    # - stoppa in som root om tom
    #else - jämför eller mindre än roten
    # avsluta när p är tomt
    #returnera p

    new_node = Node(newvalue)
    if p == None:
        p = new_node
    elif newvalue > p.value:
        if p.right == None:
            p.right = new_node
        else:
            putta(p.right, newvalue)
    elif newvalue < p.value: #gör samma sak där uppe
        putta(p.left, newvalue)
    return p

def finns(p,value): #wtf not working
    # Funktion som gör själva jobbet att söka efter ett värde
    if p.value == None:
        return False
    elif p.value == value:
        return True
    elif value > p.value:
        finns(p.right,value)
    elif value < p.value:
        finns(p.left, value)

def skriv(p):
     # Funktion som gör själva jobbet att skriva ut trädet
     if p != None: #skriver just nu bara ut första och sista....
         skriv(p.left)
         print(p.value)
         skriv(p.right)
