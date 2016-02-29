def enprint():
    
    print(encryption(raw_input()))
    
def deprint():
    print(decryption(raw_input()))
    

def encryption(x):
    pur = ("".join("{:02x}".format(ord(c)) for c in x)) 
    #Every variable will be joined with 02x which combined with .format(ord) to hexadecimal, it will split up the entire word into single hexadecimal letters.
    #The code for this was acquired from http://stackoverflow.com/questions/12214801/print-a-string-as-hex-bytes it helped a lot
    return pur

    #return main()
def decryption(x):

    dur = (''.join([chr(int(''.join(c), 16)) for c in zip(x[0::2],x[1::2])]))
    #This part of the code decrypts the hexadecimal encryption, it uses 0-15 numbers (hexadecimal) It does so by combining two userinputs (numbers) with the zip, and convert them to cha(32)
    #This code was acquired from http://stackoverflow.com/questions/9641440/convert-from-ascii-string-encoded-in-hex-to-plain-ascii
    return dur
def exit(x):
    print("Your choice: exit program")
    
    return

def main():
    print("Welcome to genericrypter")
    
    print("Please choose weather you want to encrypt, decrypt or exit the program")
    print("1 for encryption ASCII to Hexadecimal")
    print("2 for decryption Hexadecimal to ASCII")
    print("3 to end the program")
    userinput = raw_input()
    print("")
    print("You choose " + userinput)
    if userinput == "1":
        print("Your choice: encryption")
        print("Please input ASCII code")
        print("It will return its value in hexadecimal")
        enprint()        
    elif userinput == "2":
        print("Your choice: Decryption")
        print("Please input hexadecimal")
        print("It will return its value in ASCII")
        deprint()
    elif userinput == "3":
        exit(1)
#This is the main menu where you choose which program you wish to enter or weather you wish to end the program.        

main()

