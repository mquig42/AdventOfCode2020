################################################################################
# 2020-12-18
# Advent of Code 2020 Day 18
# Mike Quigley
#
# Evaluate a list of math expressions using some non-standard order of operation
# Part 2 was difficult to debug, because the input contains 348 expressions,
# and my program solved 347 of them correctly.
# Implemented someone else's algorithm, compared results, and found the one
# wrong answer I was getting. Then fixed my own algorithm.
################################################################################
import time
import re

#s: string
#idx: index of '(' char in s
#returns: The substring between idx and the matching ')' char
def bSub(s, idx):
    bCount = 0
    for i in range(idx, len(s)):
        if s[i] == '(':
            bCount += 1
        if s[i] == ')':
            bCount -= 1
        if bCount == 0:
            return s[idx:i+1]

#Evaluate an expression left to right (Part 1)
def evaluate1(s):
    #Replace brackets with the values they evaluate to
    while '(' in s:
        sub = bSub(s, s.find('('))
        s = s.replace(sub, str(evaluate1(sub[1:-1])))

    #Now that brackets are taken care of, evaluate expression from left to right
    sp = s.split(' ')
    acc = int(sp[0])
    op = sp[1]
    for i in range(2, len(sp)):
        if sp[i].isnumeric():
            if op == '+':
                acc += int(sp[i])
            elif op == '*':
                acc *= int(sp[i])
        else:
            op = sp[i]

    return acc

#Evaluate an expression with operator precedence (Part 2)
def evaluate2(s):
    #Replace brackets with the values they evaluate to
    while '(' in s:
        sub = bSub(s, s.find('('))
        s = s.replace(sub, str(evaluate2(sub[1:-1])))

    #Addition.
    while '+' in s:
        sub = re.search('\d+ \+ \d+', s).group()
        addends = re.findall('\d+', sub)
        val = str(int(addends[0]) + int(addends[1]))
        s = s.replace(sub, val, 1) #Replace ONLY THE FIRST INSTANCE of sub

    #Multiplication left to right
    sp = s.split(' ')
    acc = int(sp[0])
    for i in range(2, len(sp)):
        if sp[i].isnumeric():
            acc *= int(sp[i])

    return acc

#Entry point
start_time = time.time()

acc1 = 0
acc2 = 0
file = open('Input18.txt')
for line in file:
    line = line.strip()
    acc1 += evaluate1(line)
    acc2 += evaluate2(line)
file.close()

print('Part 1:', acc1)
print('Part 2:', acc2)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
