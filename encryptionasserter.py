import unittest
from encrdecrprog import encryption

class TestStringMethods(unittest.TestCase):

        def test_istrue(self):
                self.assertTrue(encryption('x'), 78)
if __name__ == '__main__':
        unittest.main()
              


