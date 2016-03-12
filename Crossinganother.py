class main():
    grain,man,fox,chicken = ("grain","man","fox","chicken")
    carryables = (grain,man,fox,chicken)
    forbiddens=(set((grain,chicken)),(set((fox,chicken))))
    def failure(start):
        for bank in start[0]:
            if man not in bank:
                for forbidden in failure:
                    if bank.issuperset(forbidden):
                        return True
        return False
    #Her definerer vi hva vi har og hva som ikke fungerer sammen, 
    #http://codepad.org/cywKyxXO har vi lånt koden fra
    def bankL():
        if left.bank is True:
            input(option1)
        elif left.bank is False:
            input(option2)
        else:
            print("error, bankL")
    def bankR():
        if right.bank is True:
            input(option3)
        elif right.bank is False:
            input(option4)
        else:
            print("error, bankR")
    def options():
        option1 = ()
    def victory():
        left, right = start[0]
        return left == set()
    def work(start,item):
        failureA = failure
        left.bank = bankL
        right.bank = bankR
        option1,option3 =[set(x) for x in start[0]]
        if man in bankL:
            left.bank is True
            right.bank is False
        else:
            right.bank is True
            left.bank is False
        
    start = (set((grain,man,fox,chicken)),set(()),"")
    recordstart = [start[0]]
    