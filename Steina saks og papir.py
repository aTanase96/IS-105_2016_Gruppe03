

def main():
    from random import randint
    brukervalgene = input("stein" or "saks" or papir)
    if brukervalgene == "stein":
        brukervalg = 1
    elif brukervalgene == "papir":
        brukervalg = 2
    elif brukervalgene == "saks":
        brukervalg = 3
    CpuChoice = randint(1,3) 
    if brukervalg == CpuChoice:
        print("DRAW!")
    elif brukervalg == 1 and CpuChoice== 3:
        print("Rock beats scissors PLAYER WINS!")
        main()
    elif brukervalg == 3 and CpuChoice== 1:
        print("Rock beats scissors CPU WINS")
        main()
    elif brukervalg == 1 and CpuChoice== 2:
        print("Paper beats rock CPU WINS!")
        main()
    elif brukervalg == 2 and CpuChoice== 1:
        print("paper beats rock PLAYER WINS!")
        main()
    elif brukervalg == 2 and CpuChoice== 3:
        print("Scissors beats paper CPU WINS!")
        main()
    elif brukervalg == 3 and CpuChoice== 2:
        print("Scissors beats paper PLAYER WINS!")
        main()
    elif brukervalg == 1 and CpuChoice== 2:
        print("cpu wins")
        main()
    else:
        print("Error: outcome not implemented")
main()