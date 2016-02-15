def code():
    '''
    Implements an initial table for LZW algorithm 
    '''
    table = {}
    table[1] = 'a'
    table[2] = 'b'
    table[3] = 'c'
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
    test_message = ""
    print encode(test_message)
    
test()