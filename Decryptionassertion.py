import unittest
from encrdecrprog import decryption

class TestStringMethods(unittest.TestCase):

    def test_istrue(self):
        self.assertTrue(decryption('78'), 'x')
if __name__ == '__main__':
    unittest.main()



