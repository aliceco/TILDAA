import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test_molecule_syntax(self):
        self.assertEquals(molecule_syntax("He"), "Formeln är syntaktiskt korrekt")
    def test_uppercase(self):
        self.assertEqual(molecule_syntax("h20"), "Saknda stor bokstav vid radslutet ")
        
    def test_number(self):
        self.assertEquals(molecule_syntax("Pb1"), "Siffran måste vara större än 1 ")

if __name__ =="__main__":
    unittest.main()