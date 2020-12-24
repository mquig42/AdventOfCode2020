################################################################################
# 2020-12-24
# Advent of Code 2020 Day 24
# Mike Quigley
#
# Hexagons are the bestagons. More difficult to work with than squares, though.
# See the following page for info on hex grids.
# https://www.redblobgames.com/grids/hexagons/
# Using pointy cube coords where x+y+z==0
#
# For part 2, implement a cellular automaton on the hex grid. Used a similar
# approach to day 17, the main difference being counting neighbours.
################################################################################
import time
import re

#Given a string of directions, return the coordinates of the hex it leads to
def getcoords(dirstr):
    x = 0
    y = 0
    z = 0
    for d in re.findall('se|sw|ne|nw|e|w', dirstr):
        if d == 'se':
            z += 1
            y -= 1
        elif d == 'sw':
            z += 1
            x -= 1
        elif d == 'ne':
            x += 1
            z -= 1
        elif d == 'nw':
            y += 1
            z -= 1
        elif d == 'e':
            x += 1
            y -= 1
        elif d == 'w':
            y += 1
            x -= 1
    return x, y, z

#Copied from day 17. Added offsets, so the return values can be used directly
#as loop params. Also only return X and Y, can calculate Z from (X, Y)
def getbounds(tiles):
    minX = float('inf')
    minY = float('inf')
    maxX = float('-inf')
    maxY = float('-inf')

    for c in tiles:
        minX = min(minX, c[0])
        minY = min(minY, c[1])
        maxX = max(maxX, c[0])
        maxY = max(maxY, c[1])

    minX -= 1
    minY -= 1
    maxX += 2
    maxY += 2

    return (minX, minY), (maxX, maxY)

#Returns the number of adjacent black tiles
def countneighbours(btiles, coords):
    c = 0
    x = coords[0]
    y = coords[1]
    z = coords[2]

    c += (x+1, y-1, z) in btiles
    c += (x+1, y, z-1) in btiles
    c += (x, y+1, z-1) in btiles
    c += (x-1, y+1, z) in btiles
    c += (x-1, y, z+1) in btiles
    c += (x, y-1, z+1) in btiles
    return c

def nextcycle(btiles):
    toAdd = set()
    toDel = set()

    rmin, rmax = getbounds(btiles)
    for x in range(rmin[0], rmax[0]):
        for y in range(rmin[1], rmax[1]):
            z = 0 - x - y
            if (x, y, z) in btiles:
                if not (0 < countneighbours(btiles, (x, y, z)) < 3):
                    toDel.add((x, y, z))
            elif countneighbours(btiles, (x, y, z)) == 2:
                toAdd.add((x, y, z))

    for c in toAdd:
        btiles.add(c)
    for c in toDel:
        btiles.remove(c)

#Entry point
start_time = time.time()

btiles = set() #Contains only black tiles

file = open('Input24.txt')
for line in file:
    line = line.strip()
    coords = getcoords(line)
    if coords in btiles:
        btiles.remove(coords)
    else:
        btiles.add(coords)
file.close()

print('Part 1:', len(btiles))

for i in range(100):
    nextcycle(btiles)

print('Part 2:', len(btiles))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
