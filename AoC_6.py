################################################################################
# 2020-12-06
# Advent of Code 2020 Day 6
# Mike Quigley
#
# Input file consists of a bunch of multi-line groups. For each group, count
# 1. The number of letters that appear at least once in the group
# 2. The number of letters that appear on every line in the group
# Print the total of each count.
#
# If dict didn't exist, this would have been a lot harder
################################################################################
import time

#Entry point
start_time = time.time()

count1 = 0
count2 = 0
groupSize = 0
form = dict()
file = open('Input6.txt')

for line in file:
    line = line.strip()
    if line == '':
        count1 += len(form)
        for k in form:
            if form[k] == groupSize:
                count2 += 1
        form = dict()
        groupSize = 0
    else:
        for c in line:
            if c in form:
                form[c] += 1
            else:
                form[c] = 1
        groupSize += 1

file.close()
print('Part 1:', count1)
print('Part 2:', count2)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
