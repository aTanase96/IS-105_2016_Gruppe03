def code(): #Lager en code funksjon skal code den gitte meldingen.
    '''
    Implements an initial table for LZW algorithm 
    '''
    table = {}             #Lager en tom table dictionary
    table[1] = 'a'         #Legger inn noen tegn som skal v�re i dictionaryen
    table[2] = 'b'         #Tablene auto-generere resten av tegnene til den har f�tt alle mulige varianter
    table[3] = 'c'
    table[4] = ' '
    return table

def encode(message):       #Encoder fuknsjonen som tar i bruk tabelen og funksjonen ovenfra
    table = code()         
    string = ""
    code_for_string = []
    for byte in message:    
        symbol = byte
        if (string + symbol) in table.values(): #Her finner koden stringen og symbolene i table verdiene
            string = string + symbol        #Overskriver slik at stringen best�r av b�de symbol og string
        else:
            for k,v in table.iteritems():   #Her finner koden andre symboler som ikke ligger i tablen
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol    #�ker lese "radius" med 1 plass for � f� med andre symboler/string
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print table
    return code_for_string
    
 
import urllib2
def test():  #Funksjonen som tester.
    print("write a URL")
    data = urllib2.urlopen(raw_input("")).read(20000) # leser kun 20000 karakterer
    data = data.split("\n") # og splitter den opp i linjer
    #ideen er hentet fra http://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont
    
    for line in data:
    
        print encode(line)
    
test()