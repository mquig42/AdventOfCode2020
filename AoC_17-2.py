################################################################################
# 2020-12-17
# Advent of Code 2020 Day 17 Part 2
# Mike Quigley
#
# Cellular automaton. This time, it's in an infinite 4D space.
# I'm using the same approach as part 1, just adding one more dimension.
# Dimensions are x, y, z, q with z and q starting at 0
################################################################################
import time

#Returns the number of active cells adjacent or equal to the given coords
def countAdj(x, y, z, q):
    count = 0
    for ix in range(x-1, x+2):
        for iy in range(y-1, y+2):
            for iz in range(z-1, z+2):
                for iq in range(q-1, q+2):
                    count += ((ix, iy, iz, iq) in acells)
    return count

#Returns 2 coord tuples representing the min and max corners of a bounding box
#containing all active cells
def getBounds(acells):
    minX = float('inf')
    minY = float('inf')
    minZ = float('inf')
    minQ = float('inf')
    maxX = float('-inf')
    maxY = float('-inf')
    maxZ = float('-inf')
    maxQ = float('-inf')

    for c in acells:
        minX = min(minX, c[0])
        minY = min(minY, c[1])
        minZ = min(minZ, c[2])
        minQ = min(minQ, c[3])
        maxX = max(maxX, c[0])
        maxY = max(maxY, c[1])
        maxZ = max(maxZ, c[2])
        maxQ = max(maxQ, c[3])

    return (minX, minY, minZ, minQ), (maxX, maxY, maxZ, maxQ)

#Updates acells
def nextCycle(acells):
    toAdd = set()
    toDel = set()
    
    #iterate through entire bounding box, plus one more unit in each direction
    rmin, rmax = getBounds(acells)
    for x in range(rmin[0]-1, rmax[0]+2):
        for y in range(rmin[1]-1, rmax[1]+2):
            for z in range (rmin[2]-1, rmax[2]+2):
                for q in range(rmin[3]-1, rmax[3]+2):
                    if (x, y, z, q) in acells:
                        if not (3 <= countAdj(x, y, z, q) <= 4):
                            toDel.add((x, y, z, q))
                    elif countAdj(x, y, z, q) == 3:
                        toAdd.add((x, y, z, q))
    for c in toAdd:
        acells.add(c)
    for c in toDel:
        acells.remove(c)

#Entry point
start_time = time.time()

acells = set()

file = open('Input17.txt')
for x, line in enumerate(file):
    line = line.strip()
    for y, c in enumerate(line):
        if c == '#':
            acells.add((x, y, 0, 0))
file.close()

for i in range(6):
    nextCycle(acells)
print('Part 2:', len(acells))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
