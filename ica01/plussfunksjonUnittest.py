import unittest # Importerer test bibliotek
from plussfunksjon import plussFunksjon # Henter forst filen (plussfunksjon) og henter saa metoden (plussFunksjon)

class plussTest(unittest.TestCase):
    def test(self):
        self.assertEqual(plussFunksjon(4,8), 12) # Skal sjekke hvorvidt resultatet stemmer 
        
raw_input() # Bruker maa trykke enter for aa lukke program