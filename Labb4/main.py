from bintreeFile import Bintree
from linkedQFile import LinkedQ
from bintreeFile import Bintree

#uppgift 1
# def makechildren(startord):

#     svenska = Bintree()
#     gamla = Bintree()
#     gamla.put(startord)

#     with open("Labb4/word3.txt", "r", encoding = "utf-8") as svenskfil: 
#         for rad in svenskfil:
#             ordet = rad.strip()                # Ett trebokstavsord per rad
#             if ordet in svenska:
#                 pass
#             else:
#                 svenska.put(ordet)             # in i sökträdet

#     for i in range(len(startord)):
#         alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
#         for letter in alfabet:
#             temp = list(startord)
#             temp[i] = letter
#             word = ''.join(temp)
#             if word in svenska and word not in gamla:
#                 gamla.put(word)
#                 print(word)


#uppgift 2
def makechildren(startord,slutord,q):
    gamla = Bintree()
    gamla.put(startord)
    for i in range(len(startord)):
        alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
        for letter in alfabet:
            temp = list(startord)
            temp[i] = letter
            word = ''.join(temp)
            if word in svenska and word not in gamla:
                gamla.put(word)
                print(word)

svenska = Bintree()
with open("Labb4/word3.txt", "r", encoding = "utf-8") as svenskfil: 
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)             # in i sökträdet

def main():
    start_word = input("Skriv ett startord: ").lower()
    end_word = input("Skriv ett slutord: ").lower()

    #skapa kön q
    q = LinkedQ
    

    makechildren(start_word, end_word, q)

main()