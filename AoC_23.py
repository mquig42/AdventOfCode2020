################################################################################
# 2020-12-23
# Advent of Code 2020 Day 23
# Mike Quigley
#
# The crab is rearranging cups now. My first attempt at this stored the cups
# in a standard list, and used slicing and mod to do all the insertions.
# This worked, and solved part 1 in 0.05 seconds. It was much too slow with
# a million cups, and would have taken days to solve part 2.
#
# This is a complete rewrite using dicts to implement circular linked lists.
# Not only is it faster, it's simpler.
################################################################################
import time

#Converts a list into a dict-based circular linked list
def makelist(inplist):
    newlist = dict()
    for i in range(len(inplist)-1):
        newlist[inplist[i]] = inplist[i+1]
    newlist[inplist[-1]] = inplist[0]
    return newlist

#Generate a destination list. This is used to get the destination cup number.
def makedests(cuplist):
    destlist = sorted(cuplist)
    destlist.reverse()
    return makelist(destlist)

#Makes a move. cur is value of current cup, returns value of next cup.
def move(cups, dests, cur):
    hand = []
    for i in range(3):
        hand.append(cups[cur])
        cups[cur] = cups[hand[-1]]
    
    dest = dests[cur]
    while dest in hand:
        dest = dests[dest]

    cups[hand[-1]] = cups[dest]
    cups[dest] = hand[0]
    
    return cups[cur]

#Returns ordering string to answer part 1
def p1(cups):
    r = ''
    cur = 1
    while cups[cur] != 1:
        r += str(cups[cur])
        cur = cups[cur]
    return r

#Entry point
start_time = time.time()

file = open('Input23.txt')
cuplist = [int(c) for c in file.readline().strip()]
file.close()

#Solve part 1
dests = makedests(cuplist)
cups = makelist(cuplist)
c = cuplist[0]
for i in range(100):
    c = move(cups, dests, c)

print('Part 1:', p1(cups))
print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))

#Now add a lot more cups and do it again to solve part 2
cuplist += [i for i in range(10,1000001)]

dests = makedests(cuplist)
cups = makelist(cuplist)
c = cuplist[0]
for i in range(10000000):
    c = move(cups, dests, c)

nextcup1 = cups[1]
nextcup2 = cups[nextcup1]
print('Part 2: {0} * {1} = {2}'.format(nextcup1, nextcup2, nextcup1*nextcup2))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
