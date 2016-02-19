def code():
    '''
    Implements an initial table for LZW algorithm
    '''
    table = {} #Lager en tom table dictionary
    table[1] = 't' #Legger inn noen tegn som skal v�re i dictionaryen
    table[2] = 'e' #Tablene auto-generere resten av tegnene til den har f�tt alle mulige varianter
    table[3] = 's'
    table[4] = 't '
    return table

def encode(message): #Encoder fuknsjonen som tar i bruk tabelen og funksjonen ovenfra
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in table.values(): #Her finner koden stringen og symbolene i table verdiene
            string = string + symbol #Overskriver slik at stringen best�r av b�de symbol og string
        else:
            for k,v in table.iteritems(): #Her finner koden andre symboler som ikke ligger i tablen
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol #�ker lese "radius" med 1 plass for � f� med andre symboler/string
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print table
    return code_for_string



def test():
    test_message = "unitTest"
    print encode(test_message)

test() #end
