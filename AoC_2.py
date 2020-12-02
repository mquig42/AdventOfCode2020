################################################################################
# 2020-12-02
# Advent of Code 2020 Day 2
# Mike Quigley
#
# Checks a list of passwords against 2 different validation policies
################################################################################
import time

def isValid(lo, hi, ch, pw):
    return (pw.count(ch) >= lo) and (pw.count(ch) <= hi)

def isValid2(lo, hi, ch, pw):
    clo = pw[lo-1]
    chi = pw[hi-1]
    return (clo == ch and chi != ch) or (clo != ch and chi == ch)
    

#Entry point
start_time = time.time()

count = 0
count2 = 0
inp = open('Input2.txt')
for line in inp:
    policy = line.split(': ')[0]
    pw = line.split(': ')[1]
    rg = policy.split(' ')[0].split('-')
    count += isValid((int)(rg[0]), (int)(rg[1]), policy.split(' ')[1], pw)
    count2 += isValid2((int)(rg[0]), (int)(rg[1]), policy.split(' ')[1], pw)

inp.close()

print(count, count2)
print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
