import unittest # Imports the test library
from ICA05C import list # From is the file the main code is localized in while list is the function we're adressing


testListe = ["Per", "Bajs", 1, 3] # This is a test list. Makes us able to compare and see if list intializing works as intended


class TestNewList(unittest.TestCase): # Checks if the value of the test list is ["Per", "Bajs", 1, 3]
    def setUp(self):
        pass
    def test_listIntializing(self): 
        self.assertEquals(testListe, ["Per", "Bajs", 1, 3])
        
        
class TestStandardList(unittest.TestCase): # Checks if the value of the orginal list is ["Martin", "Tor Ole", "Per-otto", "Tomas", "Andrei"]
    def setUp(self):
        pass
    def test_listIntializing(self): 
        self.assertEquals(list, ["Martin", "Tor Ole", "Per-otto", "Tomas", "Andrei"]) 
        
        
if __name__== '__main__':
    unittest.main()