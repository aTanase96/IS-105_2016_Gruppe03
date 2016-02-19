import unittest # Importerer test bibliotek
from plussFunksjon import pluss # Henter forst filen (plussFunksjon) og henter saa metoden (pluss)

class TestMinus(unittest.TestCase): # Oppretter en testklasse og intialiserer nodvendige verdier
    def setUp(self):
        pass
    def test_numbers_6_3(self):
        self.assertEqual(pluss(6,3), 9) # Skal sjekke hvorvidt resultatet stemmer

if __name__== '__main__':
    unittest.main() #end
