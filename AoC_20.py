################################################################################
# 2020-12-20
# Advent of Code 2020 Day 20
# Mike Quigley
#
# Stitch together an image from a malfunctioning camera array
# Input is a set of 10x10 tiles. 144 of them.
# Arrange them into a 12x12 square (so 120x120 pixels) by matching the pixels
# on the edge of each tile. Tiles may be flipped and/or rotated.
#
# Part 1: make a list of every edge of every tile, backwards and
# forwards. Sort the list, so matching edges will be adjacent. Can then create
# a list of neighbours. The corner tiles will have only two neighbours, instead
# of 3 for edge tiles or 4 for interior tiles.
#
# Part 2: Now it's time to stitch the whole image together. The edges aren't
# actually part of it, they're just for matching. This means that a 10x10 tile
# is actually 8x8, and the full image is 96x96
# Need to arrange all the tiles in a grid, then rotate/flip each tile,
# Then locate all the monsters in the image (which may be flipped or rotated),
# Then count the waves, which are any '#' pixels that aren't part of a monster
#
# This is by far the longest AoC program I've written this year.
# 234 sloc when my next largest is day 16 with 100
################################################################################
import time
import re

#Returns a list of all 8 edges of a given tile (4 sides, forward and reverse)
def getedges(tiles, tid):
    edges = []
    for i in [0, 9]:
        edges.append(tiles[tid][i])
        edges.append(tiles[tid][i][::-1]) #[::-1] reverses a string
        side = ''.join([line[i] for line in tiles[tid]])
        edges.append(side)
        edges.append(side[::-1])
    return edges

#Gets top row of a grid
def toprow(grid):
    return grid[0]

#gets bottom row of a grid
def bottomrow(grid):
    return grid[len(grid)-1]

#Gets left side of grid, ordered top to bottom
def leftrow(grid):
    return ''.join([line[0] for line in grid])

#Gets right side of grid, ordered top to bottom
def rightrow(grid):
    return ''.join([line[len(grid)-1] for line in grid])

#Rotates a square grid clockwise
def rotate(ingrid):
    size = len(ingrid)
    outgrid = [['.' for i in range(size)] for i in range(size)]

    for x in range(size):
        for y in range(size):
            outgrid[x][y] = ingrid[size-y-1][x]

    for i in range(size):
        outgrid[i] = ''.join(outgrid[i])
    return outgrid

#Flips a grid left to right
def flip(ingrid):
    outgrid = []
    for line in ingrid:
        outgrid.append(line[::-1])
    return outgrid

#Returns all 8 possible rotations of the given grid
def getallrotations(ingrid):
    outgrids = []
    outgrids.append(rotate(ingrid))
    outgrids.append(rotate(outgrids[-1]))
    outgrids.append(rotate(outgrids[-1]))
    outgrids.append(rotate(outgrids[-1]))
    outgrids.append(flip(ingrid))
    outgrids.append(rotate(outgrids[-1]))
    outgrids.append(rotate(outgrids[-1]))
    outgrids.append(rotate(outgrids[-1]))
    return outgrids

#Prints a grid
def printgrid(grid):
    for line in grid:
        print(line)

#Prints a grid with some character replacements to look nicer
def prettyprintgrid(grid):
    for line in grid:
        print(line.replace('.',' ').replace('#','~'))

#Sea monster detector. Returns True if the coords are the top left corner
#of a sea monster. Edits image to highlight monsters.
def ismonster(grid, x, y):
    monster = ['                  _ ',
               '\    __    __    /O>',
               ' \  /  \  /  \  /   ']

    #Check image for monster pattern
    for mx in range(len(monster)):
        for my in range(len(monster[mx])):
            if monster[mx][my] != ' ' and grid[x+mx][y+my] != '#':
                return False

    #If we reach this point, a monster has been found. Highlight it.
    for mx in range(len(monster)):
        editrow = [c for c in grid[x+mx]]
        for my in range(len(monster[mx])):
            if monster[mx][my] != ' ':
                editrow[y+my] = monster[mx][my]
        grid[x+mx] = ''.join(editrow)
            
    return True

#Returns number of sea monsters in img
def countmonsters(img):
    #Dimensions of monster pattern
    mwidth = 20
    mheight = 3
    
    mcount = 0

    for x in range(len(img) - mheight):
        for y in range(len(img[0]) - mwidth):
            mcount += ismonster(img, x, y)

    return mcount

#Returns number of waves in img, after monsters have been highlighted
def countwaves(img):
    wcount = 0
    for line in img:
        wcount += line.count('#')
    return wcount

################################################################################
#Entry point
################################################################################
start_time = time.time()

#Read input file
tiles = dict()
tile = []
tid = -1
file = open('Input20.txt')
for line in file:
    line = line.strip()
    if line.startswith('Tile'):
        tid = int(re.search('\d+', line).group())
    elif line != '':
        tile.append(line)
    else:
        tiles[tid] = tile
        tile = []
file.close()

#Make a sorted list of every edge and its tile ID
edges = []
for t in tiles:
    for e in getedges(tiles, t):
        edges.append(e + ': ' + str(t))
edges.sort()

#Init adjacency list
neighbours = dict()
for t in tiles:
    neighbours[t] = set()

#Populate adjacency list
prevedge = edges[0].split(': ')[0]
previd = int(edges[0].split(': ')[1])
for i in range(1, len(edges)):
    curedge = edges[i].split(': ')[0]
    curid = int(edges[i].split(': ')[1])
    if curedge == prevedge:
        neighbours[curid].add(previd)
        neighbours[previd].add(curid)
    prevedge = curedge
    previd = curid

#Solve part 1
p1 = 1
corners = []
for n in neighbours:
    if len(neighbours[n]) == 2:
        corners.append(n)
        p1 *= n
print('Corner tiles:', corners)
print('Part 1:', p1)
print()

#To position tiles, init a blank 12x12 grid. Put one of the known corner tiles
#in the top left position, and one of its neighbours in the next space. Now,
#fill in any remaining blank spaces based on the neighbours list
tg = [[0 for i in range(12)] for i in range(12)] #Tile Grid
tg[0][0] = min(corners)
tg[0][1] = min(neighbours[tg[0][0]])

for i in range(21):
    for x in range(11, -1, -1):
        if x > 0 and tg[x][0] == 0 and tg[x-1][0] != 0 and tg[x-1][1] != 0:
            p = neighbours[tg[x-1][0]].copy()
            p.remove(tg[x-1][1])
            if x > 1:
                p.remove(tg[x-2][0])
            tg[x][0] = p.pop()
        for y in range(11, 0, -1):
            if x == 0 and tg[x][y] == 0 and tg[x][y-1] != 0:
                p = neighbours[tg[x][y-1]].copy()
                p.remove(tg[x][y-2])
                p.remove(tg[x+1][y-1])
                tg[x][y] = p.pop()
            elif tg[x][y] == 0 and tg[x-1][y] != 0 and tg[x][y-1] != 0:
                p = neighbours[tg[x-1][y]].intersection(neighbours[tg[x][y-1]])
                p.remove(tg[x-1][y-1])
                tg[x][y] = p.pop()

print('Tile layout computed:')
printgrid(tg)
print()

#Now rotate and flip each tile so the edges match up with adjacent tiles.
for x in range(12):
    for y in range(12):
        rotations = getallrotations(tiles[tg[x][y]])
        for r in rotations:
            if x > 0:
                if (toprow(r) + ': ' + str(tg[x-1][y])) not in edges:
                    continue
            if x < 11:
                if (bottomrow(r) + ': ' + str(tg[x+1][y])) not in edges:
                    continue
            if y > 0:
                if (leftrow(r) + ': ' + str(tg[x][y-1])) not in edges:
                    continue
            if y < 11:
                if (rightrow(r) + ': ' + str(tg[x][y+1])) not in edges:
                    continue
            tiles[tg[x][y]] = r
            break
        

#At this point, everything should be correctly flipped and rotated. Assemble!
fullimg = []
for x in range(12):
    for xx in range(1, 9):
        line = ''
        for y in range(12):
            line = line + tiles[tg[x][y]][xx][1:9]
        fullimg.append(line)

rotatedimg = []
mcount = 0
for r in getallrotations(fullimg):
    mcount = countmonsters(r)
    if mcount > 0:
        rotatedimg = r
        break

prettyprintgrid(rotatedimg)
print('Found', mcount, 'sea monsters')
print('Part 2:', countwaves(rotatedimg))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
