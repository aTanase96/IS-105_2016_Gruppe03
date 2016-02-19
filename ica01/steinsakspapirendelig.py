def main():
    import random
    print ("velkommen til stein, saks og papir. Venligst velg enten stein, saks eller papir: ")
    userinput = raw_input()

    print "Du valgte: " + userinput
    #s = ("stein","saks","papir")
    s = ["stein","saks","papir"]

    cpuchoice = random.choice(s)
    print "Cpu valgte: " + cpuchoice
    if cpuchoice == "stein" and userinput == "stein":
        print("Uavgjort!")

    elif cpuchoice == "saks" and userinput == "saks":
        print("Uavgjort!")

    elif cpuchoice == "papir" and userinput == "papir":
        print("Uavgjort!")

    elif cpuchoice == "stein" and userinput == "saks":
        print("cpu vinner!")

    elif cpuchoice == "stein" and userinput == "papir":
        print("du vinner!")

    elif cpuchoice == "saks" and userinput == "stein":
        print("du vinner!")

    elif cpuchoice == "saks" and userinput == "papir":
        print("cpu vinner!")

    elif cpuchoice == "papir" and userinput == "stein":
        print("cpu vinner!")

    elif cpuchoice == "papir" and userinput == "saks":
        print("du vinner!")

    else:
        print("Error, not valid input")
    raw_input()
    main()

main()

#end
