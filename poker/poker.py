def poker(hands):
    "return the best hand"
    return max(hands, key = hand_rank)

def hand_rank(hand):
    "return a value indicating the ranking of a hand"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks)) # 2 3 4 5 6 (8,6) 6 7 8 9 T (8, 10)
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3 (7, 9 ,3 )
    elif 


def test():
    "test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker ([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    # Above statement is 99 times a list repeats that list 99 times
    return "Tests pass"

print test()