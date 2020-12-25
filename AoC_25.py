################################################################################
# 2020-12-25
# Advent of Code 2020 Day 25
# Mike Quigley
#
# We finally arrived at the hotel, but now we have to break into our own room
################################################################################
import time

#Simple brute force algorithm
def loopsize(pubkey):
    sub = 7
    v = 1
    loop = 0
    while v != pubkey:
        v *= sub
        v = v % 20201227
        loop += 1
    return loop

def transform(sub, loop):
    v = 1
    for i in range(loop):
        v *= sub
        v = v % 20201227
    return v

#Entry point
start_time = time.time()

#The description doesn't say what order the numbers are in.
#I don't think it matters, so assuming the card goes first.
file = open('Input25.txt')
cardpub = int(file.readline())
doorpub = int(file.readline())
file.close()

cardloop = loopsize(cardpub)
print('Card loop size:', cardloop)
doorloop = loopsize(doorpub)
print('Door loop size:', doorloop)
cardkey = transform(doorpub, cardloop)
print('Card encryption key:', cardkey)
doorkey = transform(cardpub, doorloop)
print('Door encryption key:', doorkey)
if cardkey == doorkey:
    print('==ACCESS GRANTED==')

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
