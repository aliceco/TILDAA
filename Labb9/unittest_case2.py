import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test_atom(self):
        self.assertEqual(readFormel("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
    
    def test_atom1(self):
        self.assertEqual(readFormel("C(OH4)C"), "Saknad siffra vid radslutet C")

    def test_atom2(self):
        self.assertEqual(readFormel("C(OH4C"), "Saknad högerparentes vid radslutet ")

    def test_atom3(self):
        self.assertEqual(readFormel("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe") #error här ger olika svar men gick genom Kattis???

    def test_atom4(self):
        self.assertEqual(readFormel("H0"), "För litet tal vid radslutet ")
    
    def test_atom5(self):
        self.assertEqual(readFormel("H1C"), "För litet tal vid radslutet C")

    def test_atom6(self):
        self.assertEqual(readFormel("H02C"), "För litet tal vid radslutet 2C")
    
    def test_atom7(self):
        self.assertEqual(readFormel("Nac1"), "Saknad stor bokstav vid radslutet c1")
    
    def test_atom8(self):
        self.assertEqual(readFormel("a"), "Saknad stor bokstav vid radslutet a")

    def test_atom9(self):
        self.assertEqual(readFormel("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
    
    def test_atom10(self):
        self.assertEqual(readFormel(")"), "Felaktig gruppstart vid radslutet )")

    def test_atom11(self):
        self.assertEqual(readFormel("2"), "Felaktig gruppstart vid radslutet 2")

if __name__ =="__main__":
    unittest.main()