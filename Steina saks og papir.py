def main():
    import random
    print ("velkommen til stein, saks og papir. Venligst velg enten stein, saks eller papir")
    userinput = input("stein" or "saks" or "papir")    
    if userinput == "stein":
        userinput = stein
    elif userinput == "saks":
        userinput == saks
    elif userinput == "papir":
        userinput = papir
        
    print ("you chose ", userinput())
    raw_input()
    s = ("stein","saks","papir")
    cpuchoice = s.split(",")
    
    if cpuchoice == "stein" and userinput == stein:
        print("Uavgjort!")
        
    elif cpuchoice == "saks" and userinput == saks:
        print("Uavgjort!")
        
    elif cpuchoice == "papir" and userinput == papir:
        print("Uavgjort!")
        
    elif cpuchoice == "stein" and userinput == saks:
        print("cpu vinner!")
        
    elif cpuchoice == "stein" and userinput == papir:
        print("du vinner!")
        
    elif cpuchoice == "saks" and userinput == stein:
        print("du vinner!")
        
    elif cpuchoice == "saks" and userinput == papir:
        print("cpu vinner!")
        
    elif cpuchoice == "papir" and userinput == stein:
        print("cpu vinner!")
        
    elif cpuchoice == "papir" and userinput == saks:
        print("du vinner!")
        
    else:
        print("Error, bugs?")
    raw_input()
main()
