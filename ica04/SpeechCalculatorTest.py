import unittest # Imports the test library
from ICA04 import taleInput # From is the file the main code is localized in while taleInput is the function we're adressing

class TestOptionOne(unittest.TestCase): # Checks if the program gives right result if user choose option five
    def setUp(self):
        pass
    def test_taleInput(self): 
        self.assertEquals == "one" # Checks if the saying "one" returns the right result. Same tests could be done for 2-5. 
        
if __name__== '__main__':
    unittest.main()
    
