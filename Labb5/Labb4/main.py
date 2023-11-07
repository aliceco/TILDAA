from Labb5.bintreeFile import Bintree
from Labb10.linkedQFile import LinkedQ


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


svenska = Bintree()
gamla = Bintree()

#lägger in filen i ett biinärträd
with open("Labb4/word3.txt", "r", encoding = "utf-8") as svenskfil: 
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)     

def makechildren(startord,slutord,q):
    gamla.put(startord) #lägger in startordet i binära trädet med dum barn
    for i in range(len(startord)): #loopar genom längden av startord
        alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
        for letter in alfabet: #byter ut en bokstav i taget
            temp = list(startord)
            temp[i] = letter
            word = ''.join(temp)
            if word in svenska and word not in gamla: # kollar om ordet finns i svenska eller gamla trädet
                if word == slutord: #om årdet gör det returnera true
                    return True 
                else: #Annars lägg i in i gamla och i kön
                    gamla.put(word) 
                    q.enqueue(word) #lägger till ordet i kön
                    print(word)
           
def main():
    startord_input = input("Skriv ett startord: ").lower()
    slutord_input = input("Skriv ett slutord: ").lower()
    # makechildren(start_word)

    q = LinkedQ()
    q.enqueue(startord_input) #lägger in startordet i kö
    while not q.isEmpty():
        startord = q.dequeue() #tar ut ur kön och sparar värdet
        if makechildren(startord, slutord_input, q): #kallar på metoden
            print(f"Det finns en väg till {slutord_input}")
            break
        elif q.isEmpty(): #om kön är tom så finns det ingen väg
            print(f"Det finns ingen väg till {slutord_input}")

        
main()