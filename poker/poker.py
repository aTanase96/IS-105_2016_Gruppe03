def poker(hands):
    "return the best hand"
    return allmax(hands, key = hand_rank)

def allmax(iterable, key=None):
    "return a list of all items equal to the max of the iterable"
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable
        xval = key(x)
        if not result or xval > maxval:
            result, maxva = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def hand_rank(hand):
    "return a value indicating the ranking of a hand"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks)) # 2 3 4 5 6 (8,6) 6 7 8 9 T (8, 10)
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3 (7, 9 ,3 )
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2,ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    "return a list of the ranks, sorted with higher first"
    ranks = ["--23456789TJQKA".index(r) for r, s in hand] # map characters to  index number
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def straight(ranks):
    "return true if the ordered ranks form a 5-card straight"
    return(max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "return true if all the cards have the same suit"
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand"""
    for r in ranks:
        if ranks.count(r) == n: return r
        return None

def two_pair(ranks):
    "if there are two pairs, return the two ranks as a tuple (highest, lowest), otherwise, return none"
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
    
    

def test():
    "test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # splits at spaces
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9 # Askinf for exact numbers - yes there is 4 of one
    assert kind(3, frkanks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7 # Again, asking for exact, and there is one seven in the hand
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5) # Here we have two 9's and two 5's
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 7, 6]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf #Straight flush
    assert poker([fk, fh]) == fk #Four of a kind
    assert poker([fh, fh]) == fh #Full house
    assert poker([sf]) == sf # Tests for one player
    assert poker ([sf] + 99*[fh]) == sf # Tests 100 players - Statement is 99 times a list repeats that list 99 times
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7) 
    assert hand_rank(fh) == (6, 10, 7)
    return "tests pass"

print test()