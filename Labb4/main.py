from bintreeFile import Bintree
from linkedQFile import LinkedQ


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


def makechildren(startord,slutord,q, svenska,gamla):
    gamla.put(startord)

    for i in range(len(startord)):
        alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
        for letter in alfabet:
            temp = list(startord)
            temp[i] = letter
            word = ''.join(temp)
            if word in svenska and word not in gamla: #söker genom svenska (binärträdet)
                if word == slutord:
                    return True
                else:
                    gamla.put(word)
                    q.enqueue(word) #lägger till ordet i kön
           
def main():
    start_word = input("Skriv ett startord: ").lower()
    end_word = input("Skriv ett slutord: ").lower()

    svenska = Bintree()
    gamla = Bintree()

    with open("Labb4/word3.txt", "r", encoding = "utf-8") as svenskfil: 
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)     

    # makechildren(start_word)
    #skapa kön q
    q = LinkedQ()
    q.enqueue(start_word)
    while not q.isEmpty():
        startord = q.dequeue()
        if makechildren(startord, end_word, q, svenska, gamla) is True:
            print(f"Det finns en väg till {end_word}")
            break
        elif q.isEmpty():
            print(f"Det finns ingen väg till {end_word}")

main()