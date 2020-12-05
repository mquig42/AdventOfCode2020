################################################################################
# 2020-12-05
# Advent of Code 2020 Day 5
# Mike Quigley
#
# Analyze everyone else's boarding pass to find the one empty seat in a full
# plane. Seats are identified by a 10-char code that describes a 2D binary
# search. Seat IDs are sequential, row * 8 + column.
# This system supports up to 128 rows, but this plane has fewer than that, so
# look for an empty seat surrounded by full ones.
#
# Part 1: Find maximum seatID
# Part 2: Find the one empty spot
################################################################################
import time

def decodeSeat(bsp):
    rMin = 0
    rRng = 128
    cMin = 0
    cRng = 8
    for c in bsp:
        if c == 'F':
            rRng = rRng // 2
        elif c == 'B':
            rRng = rRng // 2
            rMin += rRng
        elif c == 'L':
            cRng = cRng // 2
        elif c == 'R':
            cRng = cRng // 2
            cMin += cRng
    return rMin, cMin

def seatID(seat):
    return seat[0] * 8 + seat[1]

#Entry point
start_time = time.time()

IDs = []
file = open('Input5.txt')
for line in file:
    IDs.append(seatID(decodeSeat(line.strip())))
file.close()

print('Part 1:', max(IDs))

for i in range(min(IDs), max(IDs)):
    if i not in IDs:
        print('Part 2:', i)
        break

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
