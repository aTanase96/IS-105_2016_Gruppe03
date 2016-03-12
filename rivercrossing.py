class main():
    #Rivercrossing, the old man has a boat with place for one other item. He has to bring the fox, the chicken and the grain over the riverbed.
    #fox eats chicken, chicken eat grain, fox does not eat grain.
    def victory_conditions():
        goalneg = []
        goalpos = []
    def objects(object):
        man = m
        chicken = c
        grain = g
        fox = f
    def condition():
        if m and c is in boat():
            condition(a)
        elif m and g is in boat():
            condition(b)
        elif m and f is in boat():
            condition(c)
        

    def bankA(object):
        bankA = [m, c, g, f]
    def bankB(object):
        bankB = []
    def boat(object):
        boat = [bA]
    def victory():
        if m and c and g and f and boat is in bankB:
            victory(v)
    def failure():
        if c and g in bankA and m is not:
            print("Failure, chicken eats grain on the riverside")
            failure(a)
        
        elif c and f in bankA and m is not:
            print("Failure, fox eats chicken on the riverside")
            failure(d)
        elif c and g in boat and m is not:
            print("Failure, chicken eats grain in boat")
            failure(a)
        elif c and f in boat and m is not:
            print("Failure, fox eats chicken")
            failure(d)
        elif c and g in bankB and m is not:
            print("Failure, chicken eats grain on the other riverside")
            failure(a)
        elif c and g in bankB and m is not:
            print("Failure, fox eats chicken on the other riverside")
            failure(d)
        
        else:
            print("Failure")
            failure(e)
    def thehow():
        print("Try to get the fox, chicken, grain, man and the boat over to the other side without meeting any failure conditions =D")
        print("The boat can take two passangers, but it can only move with the man inside.")
        raw_input(a)
        if raw_input(a) = ("man and chicken"):
            condition(a)
        
            
            
main()