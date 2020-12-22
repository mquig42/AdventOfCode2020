################################################################################
# 2020-12-22
# Advent of Code 2020 Day 22
# Mike Quigley
#
# Play a simulated game of cards against a crab. Part 2 is a recursive variant,
# where you resolve each round by copying a subset of each deck and playing a
# full game with those copies.
#
# Though implementing all the rules takes a fair bit of code, the puzzle
# gives a detailed description of what to do here. There is room for a
# performance improvement, though. The recursive game takes 10 seconds to
# resolve, and may involve repeated sub-games with the same initial state.
# Caching the results of these sub-games could speed things up considerably.
# Already removed score calculation from playrecursive, as sub-game scores
# don't matter. This did not improve speed.
################################################################################
import time

#Simple game function for part 1. Returns winner and score
def playgame(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        winner = deck2
        if card1 > card2:
            winner = deck1
        winner.append(max(card1, card2))
        winner.append(min(card1, card2))

    winner = 2
    windeck = deck2
    if len(deck1) > 0:
        winner = 1
        windeck = deck1

    return winner, score(windeck)

#Recursive game function for part 2. Returns winner
def playrecursive(deck1, deck2):
    prevstates = set()
    while len(deck1) > 0 and len(deck2) > 0:
        #Loop detection
        curstate = getstate(deck1, deck2)
        if curstate in prevstates:
            return 1
        prevstates.add(curstate)

        cards = [deck1.pop(0), deck2.pop(0)]
        if len(deck1) >= cards[0] and len(deck2) >= cards[1]:
            winner = playrecursive(deck1[:cards[0]], deck2[:cards[1]])
            if winner == 1:
                deck1.append(cards[0])
                deck1.append(cards[1])
            else:
                deck2.append(cards[1])
                deck2.append(cards[0])
        else:
            if cards[0] > cards[1]:
                deck1.append(cards[0])
                deck1.append(cards[1])
            else:
                deck2.append(cards[1])
                deck2.append(cards[0])

    if len(deck1) > 0:
        return 1
    return 2

#Generate a string representing the state of both decks
def getstate(deck1, deck2):
    return ','.join([str(n) for n in deck1]) + '|' + ','.join([str(n) for n in deck2])

#Computes score of given deck. Works with local copy, does not edit deck.
def score(deck):
    deck = reversed(deck)
    acc = 0
    for i, c in enumerate(deck):
        acc += (i+1) * c
    return acc
    

#Entry point
start_time = time.time()

deck1 = []
deck2 = []

#Read both decks from input file
file = open('Input22.txt')
for line in file:
    if line.startswith('Player 1'):
        d = deck1
    elif line.startswith('Player 2'):
        d = deck2
    elif line != '\n':
        d.append(int(line))
file.close()

winner, s = playgame(deck1.copy(), deck2.copy())
print('Part 1: Player', winner, 'wins with final score', s)
print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))

winner = playrecursive(deck1, deck2)
s = score(deck1) + score(deck2) #Empty deck has score 0
print('Part 2: Player', winner, 'wins with final score', s)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
