import random
import sys 
""" Project Poker. In current state it will let you select any numbers of players from 1 to 9.
    It will not check wheter or not the cards match any significant values, other than the total number of drawn cards.
    It will not select same number / color more than once. This project is a result of collabration between group 3 Circut Breakers and
    group 11 Overload Factory. It would be impossible otherwise. 
"""
def main(playerNumber): # Any number from 1 - 9
    
    knight = 11
    queen = 12
    king = 13
    ace = 14  
    # Values for the picture cards, converts them to int.
    
    hearts = "Hearts"
    diamonds = "Diamonds"
    spades = "Spades"
    clubs = "Clubs"
    
    cardValue = [2, 3, 4, 5, 6, 7, 8, 9, 10, knight, queen, king, ace]
    cardColors = [hearts, diamonds, spades, clubs]
    cardsAll = []
    # Creates arrays, first one for card values, the other for card colors, and lastly cardsAll is a variable that stores
    # all card information as Card objects.
    
    x = 0
    
    
    while x < len(cardColors): # Checks if x is less than the length of the cardColors array
        y = 0
        while y < len(cardValue): # Same as above, checks Y length against cardValue array
            cardsAll.append(Card(cardValue[y], cardColors[x])) # Sums up the card value and colors and stores them in the Card array
            y += 1 
        
        x += 1
    
    random.shuffle(cardsAll) # Shuffles the card array, prevents usage of same cards (more than 4 times)
    i = 0
    players = []
    
    maxPlayers = 9
        
    playerCounter = 0
    playerHand = [] 

    
    while i < playerNumber:
        y = 0
        
        while y < 5:
            playerHand.append(cardsAll[x])
            x += 1
            y += 1
        players.append(playerHand)
        playerHand = []
        
        i += 1 # Ensures that every players recives exactly 5 cards
        
    x = 0
    while x < len(players):
        print "Player" + str(x)
        for z in players[x]:
            sys.stdout.write(str(z.getCardValue()) + " of " + z.cardColor + " ") # Ensures we get both the card value and color in printmsg
        print ""
        x += 1 
        
def getLikeValues(cardArray): # It ensures that you won't get the same cards
    temp = []
    tempValue = cardArray[0]
    cardArray.remove(tempValue)
    
    for x in cardArray:
        if x.cardValue == tempValue.cardValue:
            temp.append(x)
            temp.append(tempValue)
    return temp
        
def getScore(cardArray):
    i = 0
   # while i < len(cardArray): # Not active at current time
        
         
class Card: 
    cardColor = ""
    cardValue = 0
    
    def __init__(self, cardvalue, cardcolor):
        self.cardColor = cardcolor
        self.cardValue = cardvalue
        
    def getCardValue(self): 
        if self.cardValue > 10:
            if self.cardValue == 11: 
                return "Jack"
            elif self.cardValue == 12:
                return "Queen"
            elif self.cardValue == 13:
                return "King"
            elif self.cardValue == 14:
                return "Ace"
            else:
                return "If you get this message, something wrong happend with getCardValue method"
        elif self.cardValue == 0:
            return "If you get this message, something wrong happend with getCardValue method"
        else:
            return self.cardValue
        
            
main(4)


