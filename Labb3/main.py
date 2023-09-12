from bintreeFile import Bintree
"""
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

svenska = Bintree()
with open("Labb3/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")