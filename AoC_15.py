################################################################################
# 2020-12-15
# Advent of Code 2020 Day 15
# Mike Quigley
#
# The only difference between parts 1 and 2 is the number of iterations.
#
# For part 1 I used a list to hold previous numbers, and searched backwards to
# find the last instance of each new number. This worked well for 2020, but
# it's n^2, and much too slow for 30,000,000
#
# I'm now using a dict. The key is the number, and the value is the last time
# it was spoken. Since lookups are constant, the overall process should run
# in linear time. It still takes 14 seconds, which seems like a lot if n is
# only a few million. Could be room for improvement here, or it could be that
# going faster would require switching to a compiled language.
################################################################################
import time

#Entry point
start_time = time.time()

numCache = dict()
file = open('Input15.txt')
for i, line in enumerate(file):
    lastNum = int(line)
    numCache[lastNum] = i + 1
file.close()
del numCache[lastNum]

for i in range(len(numCache)+1, 30000000):
    if lastNum not in numCache:
        numCache[lastNum] = i
        lastNum = 0
    else:
        t = i-numCache[lastNum]
        numCache[lastNum] = i
        lastNum = t
    if i == 2019:
        print('Part 1:', lastNum)

print('Part 2:', lastNum)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
