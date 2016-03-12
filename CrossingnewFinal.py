print """
A man is trying to bring a fox, a bag of grain and a chicken across a rivercrossing. If the man does not use the boat, it cannot move across the crossing,
if the man leaves the chicken with the grain, it will eat the grain. However, leaving the chicken with the fox will mean the end of the chicken
"""

# Solution snatched from the web:
#
# The farmer brings the goat to the right side then comes back alone.
# He then takes the cabbage to the right side and brings the goat back to the left.
# He now takes the wolf to the right side and comes back alone and then
# finally takes the goat back.



man,chicken,grain,fox=("man","chicken","grain","fox")
carryables=(chicken,grain,fox,None)

# Disse kombinasjonene kan ikke skje uten hjelp
forbiddens=(set((chicken,grain)), set((fox,chicken)))

# Returnerer feil som skjer i løpet av handlingsforløpet
def mayhem(cfg):
    for shore in cfg[0]:
        if man not in shore:
            for forbidden in forbiddens:
                if shore.issuperset(forbidden):
                    return True
    return False

# Returnerer true hvis det går bra å ta fra den ene siden til den andre
def done(cfg):
    left,right=cfg[0]
    return left==set()
    
# Mannen kan enten dra over alene eller ta med seg en "item"
def ferry(cfg,item):
    left,right=[set(x) for x in cfg[0]] # make copies, because 'left' and 'right' will be mutated
    # determine on which shore the farmer is, and to which shore he will ferry
    if man in left:
        src,dst=left,right
    else:
        src,dst=right,left
    # Den neste delen vil gjøre rede for om det mannen skal transportere over er på samme side av vannet som mannen er.
    if item and not item in src:
        return None
    # Her skrives det ut om mannen går med et item eller ikke.
    desc="The man goes -->" if man in left else "The man goes <--"
    src.remove(man)
    dst.add(man)
    if item:
        src.remove(item)
        dst.add(item)
        desc+=" with the "+item
    else:
        desc+=" alone"
    return ((left,right),desc) # Her får du utskriften av det som faktisk skjer.

#Printer alle mulige kombinasjoner som er relevante.
def printcfg(cfg,level=0):
    left,right=cfg[0]
    verdict="(Not allowed)" if mayhem(cfg) else "(Ok)"
    print "    "*level,", ".join(left),"  ~~~  ",", ".join(right),cfg[1],verdict

# Hvis den har riktig input så vil den printe alle mulige kombinasjoner
def onegeneration(cfg):
    followups=[]
    for item in carryables:
        followup=ferry(cfg,item)
        if not followup: continue
        followups.append(followup)
    return followups



# start punktet
cfg=((set((man,chicken,grain,fox)), set()),"")

# Denne tar vare på tidligere konfigurasjoner
previouscfgs=[cfg[0]]

# Lager en dictionary for å printe løsningen.
solutionstack=[]
# genererer til alle mulige løsninger er skapt
def generate(cfg,level=0):
    solutionstack.extend([None]*(level-len(solutionstack)+1))
    solutionstack[level]=cfg[1]
    printcfg(cfg,level)#denne legger til handlingsforløpet som fungerer før løsningen blir lagt frem.
    childs=onegeneration(cfg)
    for child in childs:
        if mayhem(child): # her hopper den over alle problemene som ikke fungerer
            continue
        if child[0] in previouscfgs: # den gjentar ikke konfigurasjoner som allerede er gjennomført.
            continue
        previouscfgs.append(child[0])
        generate(child,level+1)
#Alt blir printet.
print "Trace of the recursive solution-finding process:" #altså den går igjennom og printer alle mulighetene som er mulige å gjennomføre uten mayham.
generate(cfg)

print "\nThe solution to the problem:"
for step in solutionstack:
    if step:
        print "  ",step
        
        
#Koden er hentet fra http://codepad.org/cywKyxXO