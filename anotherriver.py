class main():
    m, c, f, g=("man", "chicken", "fox", "grain")
    boatcarry = ('m', 'c', 'f', 'g', None)
    forbiddens = (set(('c','g')), set(('c','f')))
    
    def __innit__(self, initialValue):
        self.startState = initialValue
        self.m = 'm'
        self.c = 'c'
        self.f = 'f'
        self.g = 'g'
        self.river = river
    def bankA():
        a_dict = ['m', 'c', 'f', 'g']
        
    
    def bankB():
        b_dict = []
    def boatC():
        c_dict = []
    
    #def failure():
        #if c and g in bankA and m is not:
            #print("Failure, chicken eats grain on the riverside")
            #failure(a)
            #True
        #elif c and f in bankA and m is not:
            #print("Failure, fox eats chicken on the riverside")
            #failure(d)
            #True
        #elif c and g in boat and m is not:
            #print("Failure, chicken eats grain in boat")
            #failure(a)
            #True
        #elif c and f in boat and m is not:
            #print("Failure, fox eats chicken")
            #failure(d)
            #True
        #elif c and g in bankB and m is not:
            #print("Failure, chicken eats grain on the other riverside")
            #failure(a)
            #True
        #elif c and g in bankB and m is not:
            #print("Failure, fox eats chicken on the other riverside")
            #failure(d)
            #True
        #else:
            #print("")
            #False
            #running()
    def boat():
        if ['boat is left'] in river:
            self.remove(['boat is left'])
            self.add(['boat is right'])
        elif ['boat is right'] in river:
            self.remove(['boat is right'])
            self.add(['boat is left'])
    def mayhem(cfg):
        for shore in cfg[0]:
            if m not in bankA() or bankB():
                for forbidden in forbiddens:
                    if shore.issuperset(forbidden):
                        return True
            return False
        #Hentet fra http://codepad.org/cywKyxXO
    def victory():
        if ['m', 'c', 'f', 'g'] in bankB():
            return True
        else:
            return False
    def running():
        ['boat is left'] in river
        ['boat is empty']
        if ['boat is empty'] or ['boat uses 1 slot'] and['boat is left'] in river:
            print("The boat is on the left side of the river")
            
            for item in a_dict:
                if raw_input(a) in item:
                    a_dict.extend(c_dict)
                    del a_dict [:]
                    ['boat uses 1 slot']
                    break
                
                else:
                    print("error on item in dict")
        
        elif ['boat is empty'] or ['boat uses 1 slot'] and['boat is right'] in river:
            print("The boat is on the right side of the river")
            for item in b_dict:
                if raw_input(b) in item:
                    b_dict.extend(c_dict)
                    del b_dict [:]
                    if item in c_dict[]>1 item:
                        ['boat uses 1 slot']
                    elif item in c_dict()>2 item:
                        ['boat is filled']
                    break
                else:
                    print("Error on item in dict 2")
        
         elif ['boat is filled']             