class dealOut(object):
    deal = {}
    restOfDeck = []

def deal(numPlayers,numCards):
    from random import randint
    suits=['S','H','D','C']
    ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    deck=[]
    players={}

    # Build the Deck of Cards
    for s in suits:
        for r in ranks:
            deck.append("%s%s" % (r,s))

    # Deal cards to each player
    for x in range(numCards):
        for p in range(numPlayers):
            deal=randint(0,(len(deck)-1))
            card = deck.pop(deal)
            # Print Test to determine the order of the deal.
            # print(card)
            if x == 0:
                hand=[]
                hand.append(card)
                players['hand%s' % p]= hand
            else:
                players['hand%s' % p].append(card)


    cards = dealOut()
    cards.players = players
    cards.restOfDeck = deck
    return(cards)

# Test print
instance=deal(2,3)
print(instance.players)
print(len(instance.restOfDeck))
