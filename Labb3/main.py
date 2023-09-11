from bintreeFile import Bintree

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