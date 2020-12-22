################################################################################
# 2020-12-21
# Advent of Code 2020 Day 5
# Mike Quigley
#
# Made my day 5 program shorter
################################################################################
import time
import re

#Fun fact: if you take the boarding code and replace F and L with 0,
#B and R with 1, you get the seat ID in binary.
def binSeat(bcode):
    return int(re.sub('F|L', '0', re.sub('B|R', '1', bcode)), 2)

#Entry point
start_time = time.time()

IDs = sorted([binSeat(line.strip()) for line in open('Input5.txt')])

print('Part 1:', IDs[-1])

for i, n in enumerate(IDs):
    if IDs[i+1] != n+1:
        print('Part 2:', n+1)
        break

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
