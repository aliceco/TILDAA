from bintreeFile import Bintree
from Labb10.linkedQFile import LinkedQ

gamla = Bintree()
svenska = Bintree()

with open("Labb5/word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)  # Lägger in i trädet


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent


def writechain(end_node):
    if end_node.parent is not None:
        writechain(end_node.parent)
        print(end_node.parent.word)


def makechildren(start, end, q):
    gamla.put(start.word)
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    for i in range(len(start.word)):
        for letter in alphabet:
            temp = list(start.word)
            temp[i] = letter
            new_word = ''.join(temp)
            if new_word in svenska and new_word not in gamla:
                new = ParentNode(new_word, parent=start) #skapar ny nod med parent = gamla startordet
                if new.word == end.word:  # Avbryter om vi stöter på slutordet
                    writechain(new) #skriver ut orden i rätt ordning
                    print(end.word) 
                    return True
                else:
                    gamla.put(new.word)  # Lägger besökta ordet i 'gamla'
                    q.enqueue(new)  # Lägger besökta ordet i kön

def main():
    #skapar Node objekt av start och slutord
    startord = ParentNode(input("Skriv ett startord: ").lower()) 
    slutord = ParentNode(input("Skriv ett slutord: ").lower())
    
    q = LinkedQ()
    q.enqueue(startord)
    while not q.isEmpty():
        startord = q.dequeue()  # Tar ut ordet näst på tur i kön
        if makechildren(startord, slutord, q):
            print(f"Det finns en väg till {slutord.word}")
            break
        elif q.isEmpty():
            print(f"Det finns ingen väg till {slutord.word}")

main()