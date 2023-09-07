import unittest
from arrayQFile import ArrayQ
from linkedQFile import LinkedQ
import sys


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
#     unittest.main()"""  """


def kortlek():
    kö = ArrayQ()
    # kortlek = []
    sorterad_kortlek = []

    val = input(
        "Skriv K för att mata in kort själv, skriv R för att köra automatiskt: ")
    if val == "K" or val == "k":
        kortlek_input = input(
            "Skriv ordningen av korten med mellanslag emellan: ")
        kortlek = kortlek_input.split(" ")
    elif val == "R" or val == "r":
        kortlek = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]

    for kort in kortlek:
        kö.enqueue(int(kort))  # lägger till i en kö

    while not kö.isEmpty(): #så länge kön inte är tom
        kö.enqueue(kö.dequeue()) #lägger det översta kortet under
        sorterad_kortlek.append(kö.dequeue()) #plocksr ut det nya översta kortet och lägger till i en ny list aså att värden kan printas

    return sorterad_kortlek

#print(kortlek())


def kortlekLinkedQueue():
    kö = LinkedQ()
    sorterad_kortlek = []

    val = input(
        "Skriv K för att mata in kort själv, skriv R för att köra automatiskt: ")
    if val == "K" or val == "k":
        kortlek_input = input(
            "Skriv ordningen av korten med mellanslag emellan: ")
        kortlek = kortlek_input.split(" ")
    elif val == "R" or val == "r":
        kortlek = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]

    for kort in kortlek:
        kö.enqueue(kort)  # lägger till i en kö

    while not kö.isEmpty():
        kö.enqueue(kö.dequeue())
        sorterad_kortlek.append(kö.dequeue())

    return sorterad_kortlek

print(kortlekLinkedQueue())
