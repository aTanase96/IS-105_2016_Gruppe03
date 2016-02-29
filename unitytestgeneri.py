def main():
    #unittesting of encrdecrprog
    userinput3 = raw_input()
    A = ("".join("{:02x}".format(ord(c)) for c in userinput3))
    D = (''.join([chr(int(''.join(c), 16)) for c in zip(A[0::2],A[1::2])]))
    if D == userinput3:
        print("works")
    else:
        print("you dun goofed")
    dust = raw_input()
main()
