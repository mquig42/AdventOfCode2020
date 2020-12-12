################################################################################
# 2020-12-11
# Advent of Code 2020 Day 11 Part 2
# Mike Quigley
#
# Cellular automaton. Used recursion this time, to search for the first seat
# in each direction.
# Apart from rewriting getSeat, changes from part 1 are minimal.
################################################################################
import time

#This returns the value of the first seat in the given direction from (x, y)
#or '.' if that would be off the edge
def getSeat(seats, x, y, xv, yv):
    if (0 <= (x+xv) < len(seats)) and (0 <= (y+yv) < len(seats[0])):
        if seats[x+xv][y+yv] != '.':
            return seats[x+xv][y+yv]
        return getSeat(seats, x+xv, y+yv, xv, yv)
    return '.'

def adjCount(seats, x, y):
    r = 0
    r += getSeat(seats, x, y, -1, -1) == '#'
    r += getSeat(seats, x, y, -1,  0) == '#'
    r += getSeat(seats, x, y, -1,  1) == '#'
    r += getSeat(seats, x, y,  0, -1) == '#'
    r += getSeat(seats, x, y,  0,  1) == '#'
    r += getSeat(seats, x, y,  1, -1) == '#'
    r += getSeat(seats, x, y,  1,  0) == '#'
    r += getSeat(seats, x, y,  1,  1) == '#'
    return r

def nextRound(seats):
    n = [x[:] for x in seats]
    changed = False
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            if seats[x][y] == 'L' and adjCount(seats, x, y) == 0:
                n[x][y] = '#'
                changed = True
            if seats[x][y] == '#' and adjCount(seats, x, y) >= 5:
                n[x][y] = 'L'
                changed = True
    return n, changed

def countOccupied(seats):
    r = 0
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            r += seats[x][y] == '#'
    return r
    

#Entry point
start_time = time.time()

file = open('Input11.txt')
seats = [[c for c in line.strip()] for line in file]
file.close()

u = True
while u:
    seats, u = nextRound(seats)

print(countOccupied(seats))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
