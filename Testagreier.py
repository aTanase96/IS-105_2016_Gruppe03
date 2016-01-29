import random

class Card:
    """A card object with a suit and rank."""
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')

def __init__(self, rank, suit):
    """creates cared with rank and suit"""
    self._rank = rank
    self._suit = suit

def getRank(self):
    """return rank of card"""
    return self._rank

def getSuit(self):
    """return suit of card"""
    return self._suit

def __str__(self):
    """returns string representing card's value"""
    #Create dictionary for face cards
    translate = {11:'Jack', 12:'Queen', 13:'King', 14: 'Ace'}
    r = self._rank
    #check for face card
    if r in [11, 12, 13, 14]:
        myrank = translate[r]
    else:
        myrank = str(r)
    return myrank + " of " + self._suit


def __lt__(self, other):
    return( self._rank < other.getRank() )

class Deck:
    """Create deck of 52 cards"""

def __init__(self):
    """Return new deck of cards"""
    self._cards = []
    #Add a single card for each suit and rank
    for suit in Card.SUITS:
        for rank in Card.RANKS:
            c = Card(rank, suit)
            self._cards.append(c)


def shuffle(self):
    """Shuffle the deck"""
    random.shuffle(self._cards)

def deal(self):
    """Deals top card from deck, None if deck is empty"""
    if len(self) == 0:
        return None
    else:
        #removes top card and deals it
        return self._cards.pop()

def __len__(self):
    """returns number of cards left in the deck"""
    return len(self._cards)

def __str__(self):
    result = ""
    for c in self._cards:
        result = result + str(c) + '\n'
    return result

class Hand:
    """A hand is a list of 5 cards from Deck"""

def __init__(self, deck):
    if ( len(deck) <5):
        print ("Not enough cards in the deck!")
        return None
    self._cards = []
    for i in range(5):
        card = deck.deal()
        self._cards.append(card)
    self._myranks = [0] * 14
    self._mysuits = [0] * 4
    self.processHand()
    self._cards.sort(reverse = True)

def __str__(self):
    result = ""
    for card in self._cards:
        result = result +str(card)+ '\n'
    return result

def processHand(self):
    #get suit and rank for each card
    for card in self._cards:
        rank = card.getRank()
        rankIndex = Card.RANKS.index(rank)
        self._myranks[rankIndex] += 1
        suit = card.getSuit()
        suitIndex = Card.SUITS.index(suit)
        self._mysuits[suitIndex] += 1
    return self._myranks[rankIndex]

def myranksContains(self, n):
    return (n in self._myranks)

def mysuitsContains(self, n):
    return ( n in self._mysuits)

def hasFlush(self):
    return self.mysuitsContains(5)

def hasFourOfAKind(self):
    return self.myranksContains(3)

def hasFourOfAKindTwos(self):
    return self._myranks[0] == 4

def hasFourOfAKindThrees(self):
    return self._myranks[1] == 4

def hasFourOfAKindFours(self):
    return self._myranks[2] == 4

def hasFourOfAKindFives(self):
    return self._myranks[3] == 4

def hasFourOfAKindSixes(self):
    return self._myranks[4] == 4

def hasFourOfAKindSevens(self):
    return self._myranks[5] == 4

def hasFourOfAKindEights(self):
    return self._myranks[6] == 4

def hasFourOfAKindNines(self):
    return self._myranks[7] == 4

def hasFourOfAKindTens(self):
    return self._myranks[8] == 4

def hasFourOfAKindJacks(self):
    return self._myranks[9] == 4

def hasFourOfAKindQueens(self):
    return self._myranks[10] == 4

def hasFourOfAKindKings(self):
    return self._myranks[11] == 4

def hasFourOfAKindAces(self):
    return self._myranks[12] == 4

def hasFourOfAKind(self):
    return self.myranksContains(4)

def hasThreeOfAKind(self):
    return self.myranksContains(3)

def hasThreeOfAKindTwos(self):
    return self._myranks[0] == 3

def hasThreeOfAKindThrees(self):
    return self._myranks[1] == 3

def hasThreeOfAKindFours(self):
    return self._myranks[2] == 3

def hasThreeOfAKindFives(self):
    return self._myranks[3] == 3

def hasThreeOfAKindSixes(self):
    return self._myranks[4] == 3

def hasThreeOfAKindSevens(self):
    return self._myranks[5] == 3

def hasThreeOfAKindEights(self):
    return self._myranks[6] == 3

def hasThreeOfAKindNines(self):
    return self._myranks[7] == 3

def hasThreeOfAKindTens(self):
    return self._myranks[8] == 3

def hasThreeOfAKindJacks(self):
    return self._myranks[9] == 3

def hasThreeOfAKindQueens(self):
    return self._myranks[10] == 3

def hasThreeOfAKindKings(self):
    return self._myranks[11] == 3

def hasThreeOfAKindAces(self):
    return self._myranks[12] == 3

def hasPair(self):
    return self.myranksContains(2)

def hasPairOfTwos(self):
    return self._myranks[0] == 2

def hasPairOfThrees(self):
    return self._myranks[1] == 2

def hasPairOfFours(self):
    return self._myranks[2] == 2

def hasPairOfFives(self):
    return self._myranks[3] == 2

def hasPairOfSixes(self):
    return self._myranks[4] == 2

def hasPairOfSevens(self):
    return self._myranks[5] == 2

def hasPairOfEights(self):
    return self._myranks[6] == 2

def hasPairOfNines(self):
    return self._myranks[7] == 2

def hasPairOfTens(self):
    return self._myranks[8] == 2

def hasPairOfJacks(self):
    return self._myranks[9] == 2

def hasPairOfQueens(self):
    return self._myranks[10] == 2

def hasPairOfKings(self):
    return self._myranks[11] == 2

def hasPairOfAces(self):
    return self._myranks[12] == 2

def hasTwoPair(self):
    return self._myranks.count(2) == 2

def hasFullHouse(self):
    return self.hasPair() and self.hasThreeOfAKind()

def hasRoyalStraight(self):
    return (    self._myranks[9] == 1
                and self._myranks[10] == 1
                and self._myranks[11] == 1
                and self._myranks[12] == 1
                and self._myranks[13] == 1 )

def hasStraight(self):
    for i in range(9):
        if ( self._myranks[i]   == 1 and
             self._myranks[i+1] == 1 and
             self._myranks[i+2] == 1 and
             self._myranks[i+3] == 1 and
             self._myranks[i+4] == 1 ):
            return True
    if self.hasRoyalStraight():
        return True
    return False

def hasStraightFlush(self):
    return self.hasStraight() and self.hasFlush()

def hasRoyalFlush(self):
    return self.hasRoyalStraight() and self.hasFlush()

def score(self):
    if self.hasRoyalFlush():
        return 45
    elif self.hasStraightFlush():
        return 44
    elif self.hasFourOfAKindAces():
        return 43
    elif self.hasFourOfAKindKings():
        return 42
    elif self.hasFourOfAKindQueens():
        return 41
    elif self.hasFourOfAKindJacks():
        return 40
    elif self.hasFourOfAKindTens():
        return 39
    elif self.hasFourOfAKindNines():
        return 38
    elif self.hasFourOfAKindEights():
        return 37
    elif self.hasFourOfAKindSevens():
        return 36
    elif self.hasFourOfAKindSixes():
        return 35
    elif self.hasFourOfAKindFives():
        return 34
    elif self.hasFourOfAKindFours():
        return 33
    elif self.hasFourOfAKindThrees():
        return 32
    elif self.hasFourOfAKindTwos():
        return 31
    elif self.hasFullHouse():
        return 30
    elif self.hasFlush():
        return 29
    elif self.hasStraight():
        return 28
    elif self.hasThreeOfAKindAces():
        return 27
    elif self.hasThreeOfAKindKings():
        return 26
    elif self.hasThreeOfAKindQueens():
        return 25
    elif self.hasThreeOfAKindJacks():
        return 24
    elif self.hasThreeOfAKindTens():
        return 23
    elif self.hasThreeOfAKindNines():
        return 22
    elif self.hasThreeOfAKindEights():
        return 21
    elif self.hasThreeOfAKindSevens():
        return 20
    elif self.hasThreeOfAKindSixes():
        return 19
    elif self.hasThreeOfAKindFives():
        return 18
    elif self.hasThreeOfAKindFours():
        return 17
    elif self.hasThreeOfAKindThrees():
        return 16
    elif self.hasThreeOfAKindTwos():
        return 15
    elif self.hasTwoPair():
        return 14
    elif self.hasPairOfAces():
        return 13
    elif self.hasPairOfKings():
        return 12
    elif self.hasPairOfQueens():
        return 11
    elif self.hasPairOfJacks():
        return 10
    elif self.hasPairOfTens():
        return 9
    elif self.hasPairOfNines():
        return 8
    elif self.hasPairOfEights():
        return 7
    elif self.hasPairOfSevens():
        return 6 
    elif self.hasPairOfSixes():
        return 5
    elif self.hasPairOfFives():
        return 4  
    elif self.hasPairOfFours():
        return 3
    elif self.hasPairOfThrees():
        return 2
    elif self.hasPairOfTwos():
        return 1 
    else:
        return 0

def evaluateHand(self):
    if self.hasRoyalFlush():
        return "Royal Flush"
    elif self.hasStraightFlush():
        return "Straight Flush"
    elif self.hasFourOfAKind():
        return "Four of a Kind"
    elif self.hasFourOfAKindAces():
        return "Four of A Kind - Aces"
    elif self.hasFourOfAKindKings():
        return "Four of A Kind - Kings"
    elif self.hasFourOfAKindQueens():
        return "Four of A Kind - Queens"
    elif self.hasFourOfAKindJacks():
        return "Four of A Kind - Jacks"
    elif self.hasFourOfAKindTens():
        return "Four of A Kind - 10's"
    elif self.hasFourOfAKindNines():
        return "Four of A Kind - 9's"
    elif self.hasFourOfAKindEights():
        return "Four of A Kind - 8's"
    elif self.hasFourOfAKindSevens():
        return "Four of A Kind - 7's"
    elif self.hasFourOfAKindSixes():
        return "Four of A Kind - 6's"
    elif self.hasFourOfAKindFives():
        return "Four of A Kind - 5's"
    elif self.hasFourOfAKindFours():
        return "Four of A Kind - 4's"
    elif self.hasFourOfAKindThrees():
        return "Four of A Kind - 3's"
    elif self.hasFourOfAKindTwos():
        return "Four of A Kind - Twos"
    elif self.hasFullHouse():
        return "Full House"
    elif self.hasFlush():
        return "Flush"
    elif self.hasStraight():
        return "Straight"
    elif self.hasThreeOfAKindAces():
        return "Three of A Kind - Aces"
    elif self.hasThreeOfAKindKings():
        return "Three of A Kind - Kings"
    elif self.hasThreeOfAKindQueens():
        return "Three of A Kind - Queens"
    elif self.hasThreeOfAKindJacks():
        return "Three of A Kind - Jacks"
    elif self.hasThreeOfAKindTens():
        return "Three of A Kind - 10's"
    elif self.hasThreeOfAKindNines():
        return "Three of A Kind - 9's"
    elif self.hasThreeOfAKindEights():
        return "Three of A Kind - 8's"
    elif self.hasThreeOfAKindSevens():
        return "Three of A Kind - 7's"
    elif self.hasThreeOfAKindSixes():
        return "Three of A Kind - 6's"
    elif self.hasThreeOfAKindFives():
        return "Three of A Kind - 5's"
    elif self.hasThreeOfAKindFours():
        return "Three of A Kind - 4's"
    elif self.hasThreeOfAKindThrees():
        return "Three of A Kind - 3's"
    elif self.hasThreeOfAKindTwos():
        return "Three of A Kind - Twos"
    elif self.hasTwoPair():
        return "Two pair"
    elif self.hasPairOfAces():
        return "Pair of Aces's"
    elif self.hasPairOfKings():
        return "Pair of Kings"
    elif self.hasPairOfQueens():
        return "Pair of Queens"
    elif self.hasPairOfJacks():
        return "Pair of Jacks"
    elif self.hasPairOfTens():
        return "Pair of 10's"
    elif self.hasPairOfNines():
        return "Pair of 9's"
    elif self.hasPairOfEights():
        return "Pair of 8's"
    elif self.hasPairOfSevens():
        return "Pair of 7's"
    elif self.hasPairOfSixes():
        return "Pair of 6's"
    elif self.hasPairOfFives():
        return "Pair of 5's"
    elif self.hasPairOfFours():
        return "Pair of 4's"
    elif self.hasPairOfFours():
        return "Pair of 4's"
    elif self.hasPairOfThrees():
        return "Pair of 3's"
    elif self.hasPairOfTwos():
        return "Pair of 2's"
    else:
        return "Nothing"
    raw_input()