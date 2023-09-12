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
    new_node = Node(newvalue) #skapar nytt Nod-objekt
    if p == None: #kollar om root är tom
        p = new_node 
    elif newvalue > p.value: #kollar om nya värdet är mindre än det tidigare nod värdet
        if p.right == None: #flyttar noden till höger i trädet och kollar p.right pekar på None
            p.right = new_node
        else: #om det finns något där p.right pekar, 
            putta(p.right, newvalue) #gör om proceduren
    elif newvalue < p.value: #samma process som ovan men kollar p.left istället
        if p.left == None:
            p.left = new_node
        else:
            putta(p.left, newvalue)
    return p

def finns(p,value): #wtf not working
    # Funktion som gör själva jobbet att söka efter ett värde
    if p == None:
        return False
    if value == p.value:
        return True
    if value < p.value:
        return finns(p.left,value)
    if value > p.value:
        return finns(p.right, value)

def skriv(p):
     # Funktion som gör själva jobbet att skriva ut trädet
     if p != None: #skriver just nu bara ut första och sista....
         skriv(p.left)
         print(p.value)
         skriv(p.right)
