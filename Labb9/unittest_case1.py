import unittest
from main import *

class TestStringMethods(unittest.TestCase):
    """
        def test_molecule_syntax(self):
        self.assertEqual(molecule_syntax("He"), "Formeln är syntaktiskt korrekt")
    """    
    def test_atom(self):
        self.assertEqual(readFormel("Na"), "Formeln är syntaktiskt korrekt")

    def test_molecule(self):
        self.assertEqual(readFormel("H20"), "Formeln är syntaktiskt korrekt")
    
    def test_parenthesis(self):
        self.assertEqual(readFormel("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")

    def test_number(self):
        self.assertEqual(readFormel("Na332"), "Formeln är syntaktiskt korrekt")

if __name__ =="__main__":
    unittest.main()