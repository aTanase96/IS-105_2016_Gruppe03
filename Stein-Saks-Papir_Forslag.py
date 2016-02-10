import random

def main():
    
    print("Stein, saks, papir simulator.")
    
    valgBruker = bruker_valg()
    
    valgPC = pc_valg()
    
    resultat(valgBruker, valgPC)
    

def pc_valg():
    
    valgPC = random.randrange(1,4)
    
    if valgPC == 1:
        print("PC-en velger stein")
        
    elif valgPC == 2:
        print("PC-en velger papir")
    
    elif valgPC == 3:
        print("PC-en velger saks")

    return valgPC


def bruker_valg():
    
    valg = input("Velg 'stein', 'saks' eller 'papir' ved å skrive ordet: ")
    
    while not er_rett_valg(valg):
        print ('Det valget er feil.')
        valg = input("Velg 'stein', 'saks' eller 'papir' ved å skrive ordet: ")

    valg_tabell = {
    
        'stein' == 1,
        'papir' == 2,
        'sask'  == 3
        }
    
    return valg[(valg_tabell)]


def er_rett_valg(valg):
    return valg == 'stein' or guess == 'papir' or guess == 'saks'


def resultat(valgPC, valgBruker):
    
    forskjell = valgPC - valgBruker
    
    if forskjell == 0:
        print ("Uavgjort!")
        
    elif forskjell % 3 == 1:
        print("Beklager! Du tapte :( !")
        
    elif forkjell % 3 == 2:
        print ("Gratulerer! Du vant :) !")
