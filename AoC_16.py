################################################################################
# 2020-12-16
# Advent of Code 2020 Day 16
# Mike Quigley
#
# Input validation combined with a bit of automated puzzle solving.
# This is only the second time this year I've used a class. Having a Field
# object with a validate method makes validation easier. Can just loop through
# a list of Fields and call validate for each of them.
#
# General explanation: Create a list of all fields from the first section of
# the input file. Then put n copies of it into a grid, such that it's square
# This represents the Fields that each column in the ticket data could match.
# For each valid ticket, validate each column against all the Fields in the
# corresponding fieldGrid column. If any Field fails to validate, remove it
# from consideration for that column.
# After doing that for all the tickets, fieldGrid has been reduced, but is not
# yet down to one Field per columnn. We can reduce it further by finding any
# columns that could only match one Field, and removing that Field from the
# other columns. This does eventually get us a 1-to-1 match.
################################################################################
import time
import re

class Field:
    def __init__(self, name, ranges):
        self.name = name
        self.r1min = int(ranges[0])
        self.r1max = int(ranges[1])
        self.r2min = int(ranges[2])
        self.r2max = int(ranges[3])

    def __repr__(self):
        return self.name

    def validate(self, n):
        return (self.r1min<=n<=self.r1max) or (self.r2min<=n<=self.r2max)

#Entry point
start_time = time.time()

fields = []     #List of all fields
fieldGrid = []  #List of copies of the above list
myTicket = []   #Numbers from my ticket
invSum = 0      #Sum of all invalid fields from scanned tickets

file = open('Input16.txt')
fileZone = 0

for line in file:
    line = line.strip()
    
    if line == '':
        if fileZone == 0:
            fieldGrid = [fields[:] for i in range(len(fields))]
            
    elif line == 'your ticket:' or line == 'nearby tickets:':
        fileZone += 1
        
    elif fileZone == 0:
        fieldName = line.split(':')[0]
        fieldNums = re.findall('\d+', line)
        fields.append(Field(fieldName, fieldNums))
        
    elif fileZone == 1:
        myTicket = [int(n) for n in line.split(',')]
        
    elif fileZone == 2:
        tNums = [int(n) for n in line.split(',')]
        isValid = True
        #Search for values which are not valid for any field
        for t in tNums:
            s = 0
            for f in fields:
                s += f.validate(t)
            if s == 0:
                invSum += t
                isValid = False
        #Prune fieldGrid. For each column, remove any fields that don't validate
        if isValid:
            for i, t in enumerate(tNums):
                for f in fieldGrid[i]:
                    if not f.validate(t):
                        fieldGrid[i].remove(f)

file.close()

#Prune fieldGrid more. If a column can only be one field, then other columns
#can't also be that field
knownFields = set()
pruning = True
while pruning:
    pruning = False
    singleField = None
    for fg in fieldGrid:
        if len(fg) == 1 and fg[0] not in knownFields:
            singleField = fg[0]
            pruning = True
            break
    if pruning:
        knownFields.add(singleField)
        for fg in fieldGrid:
            if len(fg) > 1:
                fg.remove(singleField)

print('My Ticket:')
p2 = 1
for i in range(len(fields)):
    print('{0}: {1}'.format(fieldGrid[i][0], myTicket[i]))
    if fieldGrid[i][0].name.startswith('departure'):
        p2 *= myTicket[i]
print()
print('Part 1:', invSum)
print('Part 2:', p2)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
