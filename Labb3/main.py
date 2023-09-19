from Labb4.bintreeFile import Bintree
"""
uppgift 1
def makeTree():
    tree = Bintree()
    data = input("Mata in i träd: ").strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    findme = input("Mata in vad du letar efter: ").strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input("Mata in vad du letar efter: ").strip()

def main():
    tree = makeTree()
    searches(tree)
    tree.write()

main()
"""

#Uppgift 2 & 3
svenska = Bintree()
with open("Labb3/word3.txt", "r", encoding = "utf-8") as svenskfil: 
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n") 

engelska = Bintree()
meddelande = ""
with open("Labb3/engelska.txt", "r", encoding="utf-8") as engelskfil:
    for rad in engelskfil:
        orden = rad.split() # ett ord per rad
        for ordet in orden:  
            if ordet in engelska:
                pass
            else:
                engelska.put(ordet.strip())        #in i engelska sökträdet
                if ordet in svenska: #kollar om ordet finns i svenskaa sökträdet
                    meddelande += ordet + " "  #sparar ordet i en string för senare utskrift (lite onödigt men fungerar)
print(meddelande)
print("\n")