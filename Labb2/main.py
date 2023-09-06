import unittest
from arrayQFile import ArrayQ
from linkedQFile import LinkedQ


# class TestQueue(unittest.TestCase):

#     def test_isEmpty(self):
#         #isEmpty ska returnera True för tom kö, False annars
#         q = LinkedQ()
#         self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
#         q.enqueue(17)
#         self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

#     def test_order(self):
#         #Kontrollerar att kö-ordningen blir rätt
#         q = LinkedQ()
#         q.enqueue(1)
#         q.enqueue(2)
#         q.enqueue(3)
#         self.assertEqual(q.dequeue(), 1)
#         self.assertEqual(q.dequeue(), 2)
#         self.assertEqual(q.dequeue(), 3)

# if __name__ == "__main__":
#     unittest.main()


def kortlek():
    sorterad_kortlek = ArrayQ()
    kortlek = []

    val = input("Skriv K för att mata in kort själv, skriv R för att köra automatiskt: ")
    if val == "K" or val == "k":
        kortlek_input = input(
            "Skriv ordningen av korten med mellanslag emellan: ").split()
        for kort in kortlek_input:
            kort = int(kort)
            kortlek.append(kort)
    elif val == "R" or val == "r":
        kortlek = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]
        kortlek_input = kortlek  # endast för utskrift

    while len(kortlek) > 0:
        kortlek.append(kortlek.pop(0))
        sorterad_kortlek.enqueue(kortlek.pop(0))

    print(f"Inmatad kortlek: {kortlek_input}")
    print(f"Sorterad kortlek:{sorterad_kortlek}")

#kortlek()

def kortlekLinkedQueue():
    sorterad_kortlek = LinkedQ()
    kortlek = []

    val = input("Skriv K för att mata in kort själv, skriv R för att köra automatiskt: ")
    if val == "K" or val == "k":
        kortlek_input = input(
            "Skriv ordningen av korten med mellanslag emellan: ").split()
        for kort in kortlek_input:
            kort = int(kort)
            kortlek.append(kort)
    elif val == "R" or val == "r":
        kortlek = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]
        kortlek_input = kortlek  # endast för utskrift

    while len(kortlek) > 0:
        kortlek.append(kortlek.pop(0))
        sorterad_kortlek.enqueue(kortlek.pop(0))

    print(f"Inmatad kortlek: {kortlek_input}")
    print(f"Sorterad kortlek:{sorterad_kortlek}")

kortlekLinkedQueue()
