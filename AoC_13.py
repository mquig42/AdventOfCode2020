################################################################################
# 2020-12-13
# Advent of Code 2020 Day 13
# Mike Quigley
#
# My first approach to part 2, finding the largest bus number and using it as
# the step of the search loop, would have worked. It just would have taken
# a week to run. It got all the test cases, though.
#
# Second attempt is more clever: subsets are periodic. For example, the first
# two buses in my input are 23 and 37, with 37 departing 17 minutes after 23.
# This happens at timestamp 575, and every 851 minutes after that.
# I can then use 575 and 851 as the start and step in a loop that searches for
# the alignment of the first 3 bus routes, and the start and step from that
# to search for the alignment of the first 4 and so on, until I find the point
# where all the routes align.
# Because the step increases after each round, and quickly becomes very large,
# this algorithm is quite a lot faster than the first one. For my input, it
# finds an answer in less than 0.1 seconds.
################################################################################
import time

#Test if the given timestamp is a valid solution for part 2
def verify2(timestamp, busList, busOffsets):
    for b in busList:
        if (timestamp + busOffsets[b]) % b != 0:
            return False
    return True

#Entry point
start_time = time.time()

file = open('Input13.txt')
now = int(file.readline())
buses = file.readline()
file.close()

nextBus = 0
nextTime = 999999999999

busOffsets = dict()

for i, bus in enumerate(buses.split(',')):
    if bus != 'x':
        bus = int(bus)
        busOffsets[bus] = i
        acc = 0
        while acc < now:
            acc += bus
        if nextTime > acc:
            nextTime = acc
            nextBus = bus
            
print('Part 1:')
print('Bus', nextBus, 'leaves in', nextTime-now, 'minutes')
print(nextBus * (nextTime-now))
print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
print()
print('Starting part 2:')

busList = list(busOffsets)

startPoint = 0
step = busList[0]
for n in range(1, len(busList)+1):
    timestamp = startPoint
    #Search for the first alignment, to get the start point of the period
    while not verify2(timestamp, busList[:n], busOffsets):
        timestamp += step
    if n == len(busList):
        #If n includes the entire list, we only need to find the first alignment
        break
    startPoint = timestamp
    timestamp += step
    #Search for the second alignment, to calculate the length of the period
    while not verify2(timestamp, busList[:n], busOffsets):
        timestamp += step
    step = timestamp - startPoint
    print('Round {0}/{1}: Start {2} Step {3}'.format(n, len(busList), startPoint, step))
    

print('Part 2:', timestamp)
print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
