from bintreeFile import Bintree
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
"""
Uppgift 2
svenska = Bintree()
with open("Labb3/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")
"""

#Uppgift 3


svenska = Bintree()
with open("Labb3/word3.txt", "r", encoding = "utf-8") as svenskfil: 
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n") #koden kommer göra det gär först innan den kör själva uppgiften

engelska = Bintree()
meddelande = ""
with open("Labb3/engelska.txt", "r", encoding="utf-8") as engelskfil:
    for rad in engelskfil:
        orden = rad.split()
        for ordet in orden:  # Ett trebokstavsord per rad
            if ordet in engelska:
                pass
            else:
                engelska.put(ordet.strip())        # in i sökträdet
                if ordet in svenska:
                    meddelande += ordet.strip() + " "
print(meddelande)
print("\n")