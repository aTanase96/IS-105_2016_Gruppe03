
def decode(input):

    x = 0 #Brukes som counter og holder telling på hvor i inputen du er med "leseren"

    output = "" #Endelige svar som skal skrives ut på debugeren

    while x < len(input):   #While løkke, bruker lengden på inputen som parameter
        if input[x]=="0":   #Her settes hva "x"-symbolet er i binær
            output += "x"   #Her skrives det til output-variabelen

        elif input[x]=="1" and input[x + 1]=="0": #Mye av koden er lik, så trenger ikke kommentar til alt. :)
            output += "y"
            x += 1

        elif input[x]=="1" and input[x + 1]=="1":
            output += "z"
            x += 1

        x += 1

    return output


print decode("00101001100000")


def code(input):
    x = 0

    output = ""

    while x < len(input):
        if input[0]=="x":
            output +="0"

        elif input[10]=="y":
            output += "10"
            x += 1
        elif input[11]=="z":
            output +="11"
            x += 1

        x += 1

    return output

print code("xx")

#end
