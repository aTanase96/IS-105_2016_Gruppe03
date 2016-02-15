import binascii

binary2ascii = {}

ascii2binary = {}


textfile = open('sourcecode.txt', "r")

textinput = ""

for x in textfile: 
    textinput += str(x) 


for i in range(0,128): 
    ascii2binary[chr(i)] = format(i,"08b")
    

for i in range(0,128):
    binary2ascii[format(i,"08b")] = chr(i)



counter = 0

x = 0

output = ""

temp = ""

#print textinput

while counter < len(textinput): 
    if x < 8: 
        temp += textinput[counter]
        x += 1
        
    if x == 8: 
        output += binary2ascii[temp]
        temp = ""
        x = 0        
    counter += 1

     
     
print output
