from Labb4.linkedQFile import LinkedQ

def kortlekLinkedQueue():
    kö = LinkedQ()
    sorterad_kortlek = []

    indata = input("Input: ")
    kortlek = indata.split(" ")

    for kort in kortlek:
        kö.enqueue(kort)  # lägger till i en kö

    while not kö.isEmpty():
        kö.enqueue(kö.dequeue())
        sorterad_kortlek.append(kö.dequeue())

    return sorterad_kortlek

resultat = ""

for element in kortlekLinkedQueue():
    resultat += str(element) + " "


print(resultat)