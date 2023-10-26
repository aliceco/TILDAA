import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test_molecule_syntax(self):
        self.assertEqual(molecule_syntax("He"), "Formeln är syntaktiskt korrekt")
        
    def test_number(self):
        self.assertEqual(molecule_syntax("Pb1"), "För litet tal vid radslutet")

    def test_uppercase(self):
        self.assertEqual(molecule_syntax("h20"), "Saknad stor bokstav vid radslutet h20")

if __name__ =="__main__":
    unittest.main()