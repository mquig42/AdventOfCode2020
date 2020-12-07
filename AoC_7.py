################################################################################
# 2020-12-07
# Advent of Code 2020 Day 7
# Mike Quigley
#
# Looks like this is where things start to get interesting (using the
# definition from Serenity). Most of the planning for this revolved around
# data structures. Because parts 1 and 2 are the reverse of each other, they
# are best solved with different data structures.
#
# Part 1 uses a dict of sets, in inside-out order.
# containers['shiny gold'] is a set of all bags which directly contain 1 or more
# shiny gold bags.
# Once I had that, I could write a recursive function to deal with nesting.
#
# Part 2 uses a more straightforward dict of dicts
# contents['shiny gold'] represents the direct contents of a shiny gold bag.
# For example, my test input has 'shiny gold bags contain 4 light blue bags',
# so contents['shiny gold']['light blue'] == 4
# Again I used a recursive function to deal with nesting and add up the total.
################################################################################
import time
import re

#Get a set of all possible colours which could contain the given colour
def getContainers(bags, colour):
    if colour not in bags:
        return set()
    r = bags[colour].copy()
    for c in bags[colour]:
        r.update(getContainers(bags, c))
    return r

#Return the total number of bags contained inside a bag of given colour
def countContents(bags, colour):
    r = 0
    if colour in bags:
        for c in bags[colour]:
            r += bags[colour][c]
            r += (bags[colour][c] * countContents(bags, c))
    return r

#Entry point
start_time = time.time()

containers = dict()
contents = dict()

file = open('Input7.txt')
for line in file:
    line = line.strip()
    container = re.match('\w+\W\w+', line).group()
    contents[container] = dict()
    for c in re.findall('\d+ \w+ \w+', line):
        n = int(re.match('^\d+',c).group())
        c = c.lstrip('1234567890 ')
        contents[container][c] = n
        if c not in containers:
            containers[c] = set()
        containers[c].add(container)

print('Part 1:', len(getContainers(containers, 'shiny gold')))
print('Part 2:', countContents(contents, 'shiny gold'))

#Just for fun, combine parts 1 and 2. Which of the possible outermost bags
#from part 1 will contain the maximum number of bags
maxCount = 0
maxBag = ''
for bag in getContainers(containers, 'shiny gold'):
    cc = countContents(contents, bag)
    if cc > maxCount:
        maxCount = cc
        maxBag = bag
print('Part 3:', maxBag, maxCount)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
