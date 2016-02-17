import unittest # Imports the test library
from LZWDecoding import encode

class TestEncodeFunction(unittest.TestCase): # Creates the test class and gives it the name of the function we are testing
    def setUp(self):
        pass
    def test_encodeMessage(self): 
        self.assertEquals(encode('unitTest'), [5, 1, 2, 3, 1])  
        print self.test_encodeMessage
        
if __name__== '__main__':
    unittest.main()
    
"""The test above tests the "encode" function in "LZWDecoding" file. The test checks if the function "encode" works as intented.""" 