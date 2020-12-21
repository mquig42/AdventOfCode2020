################################################################################
# 2020-12-21
# Advent of Code 2020 Day 21
# Mike Quigley
#
# Much shorter problem than the last two days. The input file is only 36 lines.
# There are 8 allergens and 199 different ingredients.
#
# For each allergen, make a set of all the ingredients that are in
# every food with that allergen. Ingredients that aren't in any of those sets
# are safe. Mapping ingredients to allergens is a similar problem to day 16.
# This time I used sets instead of lists. The intersection function was
# very useful in part 1.
################################################################################
import time

class food:
    def __init__(self, line):
        self.ingredients = set()
        self.allergens = set()
        for i in line.split(' (contains ')[0].split(' '):
            self.ingredients.add(i)
        for a in line.replace(')','').split(' (contains ')[1].split(', '):
            self.allergens.add(a)

#Entry point
start_time = time.time()

ingredients = set()     #Full set of all ingredients
allergens = dict()      #Full set of all allergens
foods = []              #List of foods. Each one has its own sets

file = open('Input21.txt')
for line in file:
    line = line.strip()
    foods.append(food(line))
    for i in line.split(' (contains ')[0].split(' '):
        ingredients.add(i)
    for a in line.replace(')','').split(' (contains ')[1].split(', '):
        allergens[a] = set()
file.close()

for a in allergens:
    for f in foods:
        if a in f.allergens:
            if len(allergens[a]) == 0:
                allergens[a] = f.ingredients.copy()
            else:
                allergens[a].intersection_update(f.ingredients)

safe = ingredients.copy()
for a in allergens:
    safe.difference_update(allergens[a])

p1 = 0
for s in safe:
    for f in foods:
        if s in f.ingredients:
            p1 += 1

print('Part 1:', p1)

#This is similar to the train ticket matching on day 16
dangerous = set()
pruning = True
while pruning:
    pruning = False
    for a in allergens:
        if len(allergens[a]) == 1 and allergens[a].isdisjoint(dangerous):
            for a2 in allergens:
                if len(allergens[a2]) > 1:
                    allergens[a2].difference_update(allergens[a])
                    pruning = True
            dangerous.update(allergens[a])

p2 = ''
for a in sorted(allergens):
    ingredient = allergens[a].pop()
    print(a, ':', ingredient)
    p2 += ingredient + ','
p2 = p2.rstrip(',')
print('Part 2:', p2)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
