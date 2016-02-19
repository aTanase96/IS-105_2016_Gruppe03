import unittest # Importerer test bibliotek
from Minusv4 import minus # Henter forst filen (Minusv4) og henter saa metoden (minus)

class TestMinus(unittest.TestCase): # Oppretter en testklasse og intialiserer nodvendige verdier
    def setUp(self):
        pass
    def test_numbers_6_3(self):
        self.assertEqual(minus(6,3), 3) # Skal sjekke hvorvidt resultatet stemmer

if __name__== '__main__':
    unittest.main()

    #end
