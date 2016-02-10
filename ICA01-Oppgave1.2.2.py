
def code(input):
    
    x = 0

    output = ""

    while x < len(input):
        if input[x]=="0":
            output += "x"
            
        elif input[x]=="1" and input[x + 1]=="0":
            output += "y"
            x += 1
            
        elif input[x]=="1" and input[x + 1]=="1":
            output += "z"
            x += 1
            
        x += 1
        
    return output
            
            
print code("00101001100000")

    
    
    









