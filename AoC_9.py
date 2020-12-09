################################################################################
# 2020-12-09
# Advent of Code 2020 Day 9
# Mike Quigley
#
# All array operations this time. For part 1, find the first value that isn't
# the sum of 2 distinct numbers out of the previous 25.
# For part 2, find a continuous range with a sum equal to the answer for part 1
#
# The helpful Python feature of the day is array slicing. sum(data[i:j]) FTW
################################################################################
import time

#Returns True if n is the index to part 1's answer
def isSum(data, n):
    dataSub = data[n-25:n]
    for i in dataSub:
        if data[n] - i in dataSub and (data[n] - i) != i:
            return True
    return False

#Entry point
start_time = time.time()

file = open('Input9.txt')
data = [int(line.strip()) for line in file]
file.close()

p1 = 0
for i in range(25, len(data)):
    if not isSum(data, i):
        p1 = data[i]
        break

i = 0
j = 0
while True:
    if sum(data[i:j]) == p1:
        break
    elif sum(data[i:j]) < p1:
        j += 1
    else:
        i += 1

print('Part 1:', p1)
print('Part 2:', min(data[i:j]) + max(data[i:j]))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
