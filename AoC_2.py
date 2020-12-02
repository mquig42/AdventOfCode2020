################################################################################
# 2020-12-02
# Advent of Code 2020 Day 2
# Mike Quigley
#
# Checks a list of passwords against 2 different validation policies
################################################################################
import time

def isValid(policy, pw):
    lo = (int)(policy.split(' ')[0].split('-')[0])
    hi = (int)(policy.split(' ')[0].split('-')[1])
    ch = policy.split(' ')[1]
    return (pw.count(ch) >= lo) and (pw.count(ch) <= hi)

def isValid2(policy, pw):
    lo = (int)(policy.split(' ')[0].split('-')[0])
    hi = (int)(policy.split(' ')[0].split('-')[1])
    ch = policy.split(' ')[1]
    clo = pw[lo-1]
    chi = pw[hi-1]
    return (clo == ch and chi != ch) or (clo != ch and chi == ch)
    

#Entry point
start_time = time.time()

count = 0
count2 = 0
inp = open('Input2.txt')
for line in inp:
    if isValid(line.split(': ')[0],line.split(': ')[1]):
        count = count + 1
    if isValid2(line.split(': ')[0],line.split(': ')[1]):
        count2 = count2 + 1

print(count, count2)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
