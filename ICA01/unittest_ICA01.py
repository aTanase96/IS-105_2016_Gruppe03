import unittest

from ICA01Oppgave1 import decode

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_7(self):
        self.assertEqual(decode("00101001100000"), "xxyyxzxxxxx")
        
if __name__ == '__main__':
    
    unittest.main()
    