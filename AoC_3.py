################################################################################
# 2020-12-03
# Advent of Code 2020 Day 3
# Mike Quigley
#
# The input file is a repeating grid of trees. Find the number of trees
# you would encounter if you went from the top left of the grid to the bottom
# in a straight line determined by a constant slope (eg. slope=3 means 1 down,
# 3 right)
# Part 1 uses slope=3, part 2 takes several slopes and multiplies their tree
# counts together.
################################################################################

import time

def isTree(grid, y, slope):
    x = (int)((y * slope) % len(grid[0]))
    return grid[y][x] == '#'

#Entry point
start_time = time.time()

file = open('Input3.txt')
grid = [line.strip() for line in file]
file.close()

treeCount = [0, 0, 0, 0, 0]
for i in range(len(grid)):
    treeCount[0] += isTree(grid, i, 1)
    treeCount[1] += isTree(grid, i, 3)
    treeCount[2] += isTree(grid, i, 5)
    treeCount[3] += isTree(grid, i, 7)
    if i % 2 == 0:
        treeCount[4] += isTree(grid, i, 0.5)

product = 1
for t in treeCount:
    product = product * t

print(treeCount[1], product)
print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
