################################################################################
# 2020-12-11
# Advent of Code 2020 Day 11 Part 1
# Mike Quigley
#
# Cellular automaton
################################################################################
import time

def getSeat(seats, x, y):
    if (0 <= x < len(seats)) and (0 <= y < len(seats[0])):
        return seats[x][y]
    return '.'

def adjCount(seats, x, y):
    r = 0
    r += getSeat(seats, x-1, y-1) == '#'
    r += getSeat(seats, x-1, y) == '#'
    r += getSeat(seats, x-1, y+1) == '#'
    r += getSeat(seats, x, y-1) == '#'
    r += getSeat(seats, x, y+1) == '#'
    r += getSeat(seats, x+1, y-1) == '#'
    r += getSeat(seats, x+1, y) == '#'
    r += getSeat(seats, x+1, y+1) == '#'
    return r

def nextRound(seats):
    n = [x[:] for x in seats]
    changed = False
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            if seats[x][y] == 'L' and adjCount(seats, x, y) == 0:
                n[x][y] = '#'
                changed = True
            if seats[x][y] == '#' and adjCount(seats, x, y) >= 4:
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
