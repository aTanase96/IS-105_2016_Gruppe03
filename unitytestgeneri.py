import unittest
from encrdecrprog import encryption
import random
from encrdecrprog import decryption
from Crypto.Cipher import AES
class test(unittest.TestCase):
    def encryption(encryption):
        initialization_vector = Random.new().read(AES.block_size)
        cipher = AES.new(settings.secret, AES.MODE_CFB, initialization_vector)
        return initialization_vector + cipher.encrypt(bytes(encryption.encode('Hexadecimal')))
    def decryption(decryption):
        initialization_vector, decryption = decryption[:AES.block_size], crypt[AES.block_size:]
        cipher = AES.new(settings.secret, AES.MODE_CFB, initialization_vector)
        return cipher.decryption(decryption)        
    def test_encrypt(self):

    encryption = utils.encryption("abcdefg")
    self.assertEquals(encryption)  
if __name__ == '__main__':
    unittest.main()