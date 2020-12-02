################################################################################
# 2020-12-01
# Advent of Code 2020 Day 1
# Mike Quigley
#
# Find 2 or 3 numbers in input file that add to 2020, and multiply them
################################################################################
import time

#Part 1: Find 2 numbers
def part1(expenses):
    for x in expenses:
        for y in expenses:
            if x + y == 2020:
                print(x,'*',y,'=',x*y)
                return

#Part 2: Find 3 numbers
def part2(expenses):
    for x in expenses:
        for y in expenses:
            for z in expenses:
                if x + y + z == 2020:
                    print(x,'*',y,'*',z,'=',x*y*z)
                    return

#Entry point
start_time = time.time()

file = open('input1.txt')

expenses = []
for line in file:
    expenses.append((int)(line.strip()))

file.close()

part1(expenses)
part2(expenses)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
