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

with open("Labb3/engelska.txt", "r", encoding= "utf-8") as engelskfil:
    for rad in engelskfil:
        print(rad.strip())

"""
engelska filen
Måste ta bort tomma rader
måste separera orden baserat på split
måste ta bort "-tecken och punkter och '-tecken och !-tecken (alltså en jävla massa tecken)
"""

"""
vi ska använda uppgift 2
vi får ord - kollar om det finns i engelska ordlistan
om nej - stoppa in
om ja - kolla om det oxå finns i svenska
    om ja - kolla om finns i utskriften
        om ja - ingenting
        om nej - skriv ut
    om nej - ingenting

"""