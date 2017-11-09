# Determine if a shuffled deck of cards is legitimately a shuffled version of two half-decks

def isRiffle(shuffled_deck, half1, half2):

    for card in shuffled_deck:
        if len(half1) != 0 and card == half1[0]:
            half1.pop(0)
        elif len(half2) != 0 and card == half2[0]:
            half2.pop(0)
        else:
            return False
    return True