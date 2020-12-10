################################################################################
# 2020-12-10
# Advent of Code 2020 Day 10
# Mike Quigley
#
# Joltage adapters always increase the joltage by up to 3? So you can turn
# 0 into 3? Seems like the thermodynamics police might want to investigate.
#
# Part 1 is easy, just sort the list and iterate through once, comparing each
# value to the previous.
# Part 2 was more difficult. After some thought, and reviewing some graph theory
# I decided to model the possible connections between adapters as a directed
# acyclic graph. In theory, a depth first search could count each path, but
# would probably be extremely slow. Instead, I went through the adapter list
# in reverse order, caching the number of paths. That way I could just sum up
# all the children.paths instead of actually exploring each path to the end.
################################################################################
import time

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.paths = 0

#Given a sorted list of adapters (including initial zero and final device),
#count the number of 1 and 3 jolt differences, return the product
def count13(adapters):
    ones = 0
    threes = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i-1] == 1:
            ones += 1
        elif adapters[i] - adapters[i-1] == 3:
            threes += 1
    return ones * threes

#Solve part 2 using a directed acyclic graph
def countPaths(adapters):
    #Create graph nodes
    nodes = dict()
    for a in adapters:
        nodes[a] = GraphNode(a)

    #Connect graph nodes
    for a in adapters:
        if a + 1 in nodes:
            nodes[a].children.append(nodes[a+1])
        if a + 2 in nodes:
            nodes[a].children.append(nodes[a+2])
        if a + 3 in nodes:
            nodes[a].children.append(nodes[a+3])

    #Iterate backwards through list
    adapters.reverse()
    for a in adapters:
        if len(nodes[a].children) == 0:
            nodes[a].paths = 1
        else:
            for c in nodes[a].children:
                nodes[a].paths += c.paths

    return nodes[0].paths

#Entry point
start_time = time.time()

file = open('Input10.txt')
adapters = [int(line.strip()) for line in file]
file.close()

adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

print('Part 1:', count13(adapters))
print('Part 2:', countPaths(adapters))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
