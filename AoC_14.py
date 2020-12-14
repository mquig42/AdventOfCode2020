################################################################################
# 2020-12-14
# Advent of Code 2020 Day 14
# Mike Quigley
#
# An interesting problem. I used lists of chars for all my bit manipulation,
# which may be suboptimal. Lots of conversions.
# Textfile -> string -> int -> string -> charlist -> string -> int
#
# In part 2, to generate a list of all matching memory addresses, I used 2 lists
# matches contains charlists which still have Xes in them
# nXmatches contains charlists with no Xes.
# As long as matches is not empty, I take the first item in it, create 2 copies,
# replace the first X in each copy with a 0 or 1, then append the copies into
# either matches or nXmatches depending on if they have any more Xes.
################################################################################
import time
import re

#Apply bitmask to n using rules from part 1. This is done by converting n
#from an int to a string to a list of chars, applying the mask, then going back
#to a string and then an int. Surprisingly, this works and isn't horribly slow.
def applyMask(n, mask):
    nBits = [c for c in '{0:b}'.format(n).zfill(36)]
    for i in range(36):
        if mask[i] != 'X':
            nBits[i] = mask[i]
    return int(''.join(nBits), 2)

#Applies mask to memory address using rules from part 2. Returns list of matches
def decodeAddr(n, mask):
    matches = []
    nXmatches = []
    nBits = [c for c in '{0:b}'.format(n).zfill(36)]
    for i in range(36):
        if mask[i] != '0':
            nBits[i] = mask[i]
    matches.append(nBits)

    while len(matches) > 0:
        m = matches.pop(0)
        if 'X' in m:
            i = m.index('X')
            m0 = m.copy()
            m1 = m.copy()
            m0[i] = '0'
            m1[i] = '1'
            if 'X' in m0:
                matches.append(m0)
                matches.append(m1)
            else:
                nXmatches.append(m0)
                nXmatches.append(m1)
        else:
            nXmatches.append(m)

    return [int(''.join(m), 2) for m in nXmatches]
            

#Entry point
start_time = time.time()

mem1 = dict()
mem2 = dict()
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

file = open('Input14.txt')
for line in file:
    line = line.strip()
    if line.startswith('mask'):
        mask = line[7:]
    else:
        parsedLine = re.findall('\d+',line)
        mem1[int(parsedLine[0])] = applyMask(int(parsedLine[1]), mask)
        for a in decodeAddr(int(parsedLine[0]), mask):
            mem2[a] = int(parsedLine[1])
file.close()

acc = 0
for a in mem1:
    acc += mem1[a]
print('Part 1:', acc)

acc = 0
for a in mem2:
    acc += mem2[a]
print('Part 2:', acc)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
