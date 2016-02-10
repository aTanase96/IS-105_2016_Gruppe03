def code():
    '''
    Implements an initial table for LZW algorithm 
    '''
    table = {}
    table[1] = 'T'
    table[2] = 'o'
    table[3] = 'b'
    table[4] = 'e'
    table[5] = 'r'
    table[6] = 'n'
    table[7] = 't'
    table[8] = ' '
    return table

def encode(message):
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in table.values():
            string = string + symbol
        else:
            for k,v in table.iteritems():
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print table
    return code_for_string
    
    

def test():
    test_message = "To be or not to be"
    print encode(test_message)
    
test()