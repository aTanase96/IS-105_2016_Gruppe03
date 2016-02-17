import unittest # Imports the test library
from LZWDecoding import code

class TestCodeFunction(unittest.TestCase): # Creates the test class and gives it the name of the function we are testing
    def setUp(self):
        pass
    def test_codeArray(self): 
        self.assertEquals(code(), {1: 't', 2: 'e', 3: 's', 4: 't '})  
        print self.test_codeArray
        
if __name__== '__main__':
    unittest.main()
    
"""The test above tests the "code" function in "LZWDecoding" file. The test checks if the function "code" creates an array / table with the 
following letters (numbers is the index the letter is placed on, example "t" in on index 1): {1: 't', 2: 'e', 3: 's', 4: 't'}""" 