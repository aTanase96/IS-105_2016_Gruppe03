import math # Importerer mattebibliotek

tall1 = (input("Velg det forste tallet: "))
tall2 = (input("Velg det andre tallet som skal plusses med det forste: "))

def pluss(tall1, tall2):
    return tall1 + tall2

print "Du plusset de to tallene sammen, og fikk:", pluss

print "Trykk enter for aa lukke vinduet"

raw_input() # Bruker maa trykke enter for aa lukke programm
