def code():
    
    table = {}
    table[1] = "X"
    table[2] = "Y"
    table[3] = "Z"
    return table

textfile = open('BS.txt', "r")
textinput = ""


for x in textfile:
    textinput += str(x)
    
x = 0

counter = 0

temp = ""

output = ""

while counter < len(textfile):
    if x < 14:
        temp += textinput[counter]
        x += 1 
    
    
    
    









