################################################################################
# 2020-11-04
# Advent of Code 2020 Day 4
# Mike Quigley
#
# Today's input file represents passports. Make sure each one has all the
# required fields, except cid (because a North Pole ID doesn't have that, and
# we're being sneaky)
# Part 2 checks the fields for invalid values
################################################################################
import time
import re

def isValid1(p):
    for f in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
        if f not in p:
            return False
    return True

def isValid2(p):
    if (int)(p['byr']) < 1920 or (int)(p['byr']) > 2002:
        return False
    
    if (int)(p['iyr']) < 2010 or (int)(p['iyr']) > 2020:
        return False
    
    if (int)(p['eyr']) < 2020 or (int)(p['eyr']) > 2030:
        return False

    hv = (int)(p['hgt'][:-2])   #height value
    hu = p['hgt'][-2:]          #height unit
    if not ((150<=hv<=193 and hu=='cm') or (59<=hv<=76 and hu=='in')):
        return False

    if not re.match('^#[0-9a-f]{6}$',p['hcl']):
        return False

    if p['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False

    if not re.match('^[0-9]{9}$',p['pid']):
        return False

    return True

#Entry point
start_time = time.time()

validCount1 = 0
validCount2 = 0
passport = dict()
file = open('Input4.txt')

for line in file:
    line = line.strip()
    if line == '':
        if isValid1(passport):
            validCount1 += 1
            validCount2 += isValid2(passport)
        passport = dict()
    else:
        for kvp in line.split(' '):
            passport[kvp.split(':')[0]] = kvp.split(':')[1]

file.close()

print(validCount1, validCount2)
print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
