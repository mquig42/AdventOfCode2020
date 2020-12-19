################################################################################
# 2020-12-19
# Advent of Code 2020 Day 19 Part 2
# Mike Quigley
#
# Match text against a rule system. Rules are numbered, and may be one of
# 0: 4 1 5     - Ordered sequence of other rules
# 1: 2 3 | 3 2 - Pipe represents OR, so (2 3) or (3 2). Max one pipe per rule
# 4: "a"       - Single letter
#
# Use a recursive function that takes string and rule number, returns either -1
# if no match, or index of last matching char + 1.
# If m matches rule 0, then match(rules, '0', m) will return len(m)
# What if both options of | rule match different lengths of the string?
#  -Pick one value at random. This will work some of the time.
#   Simply run the program repeatedly, and it's likely to find every match
################################################################################
import time
import random

#Main recursive matching function
def match(rules, r, m, start):
    #Trivial non-matches
    if start == -1:
        return -1
    elif start >= len(m):
        return -1

    #Terminal rules. Since there are only two, I hard-coded them
    elif rules[r] == '"a"':
        if m[start] == 'a':
            return start + 1
        else:
            return -1
    elif rules[r] == '"b"':
        if m[start] == 'b':
            return start + 1
        else:
            return -1

    #If there's no |, can just call match_seq once
    elif '|' not in rules[r]:
        return match_seq(rules, rules[r], m, start)

    #There is a |, so test each branch
    else:
        seqs = rules[r].split(' | ')
        matches = set()
        for seq in seqs:
            matches.add(match_seq(rules, seq, m, start))
        matches.discard(-1)
        if len(matches) == 0:
            return -1
        elif len(matches) == 1:
            return matches.pop()
        else:
            #If there's more than one matching rule, return one at random
            return random.choice([i for i in matches])

#Checks message m against a linear sequence of rules. Useful for checking
#one branch of a | rule
def match_seq(rules, rule, m, start):
    idx = start
    for sr in rule.split(' '):
        idx = match(rules, sr, m, idx)
    return idx

#Entry point
start_time = time.time()

rules = dict()
messages = []
matches = set()

sec = 0
file = open('Input19.txt')
for line in file:
    line = line.strip()
    if line == '':
        sec += 1
    if sec == 0:
        lsplit = line.split(': ')
        rules[lsplit[0]] = lsplit[1]
    elif sec == 1:
        #Don't match here, just put all messages in a list
        messages.append(line)
file.close()

#Modify rules for part 2
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

#Try matching the list against rule 0 100 times. Keep track of matches in a set
for i in range(100):
    for msg in messages:
        if match(rules, '0', msg, 0) == len(msg):
            matches.add(msg)

print('Part 2:', len(matches))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
