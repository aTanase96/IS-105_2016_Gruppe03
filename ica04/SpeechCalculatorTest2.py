import unittest # Imports the test library
from ICA04 import taleInput # From is the file the main code is localized in while taleInput is the function we're adressing

class TestOptionOne(unittest.TestCase): # Checks if the program gives right result if user choose option five
    def setUp(self):
        pass
    def test_taleInput(self): 
        self.assertEquals == "five" # Checks if the saying "five" retuns the right value, in this case quitting.
        
if __name__== '__main__':
    unittest.main()