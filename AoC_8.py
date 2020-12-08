################################################################################
# 2020-12-08
# Advent of Code 2020 Day 8
# Mike Quigley
#
# This challenge involves running something that resembles assembly language.
# The only instructions are ACC, which adds a value to a register, and JMP.
# In part 1, the code contains an infinite loop. I used a set of previously
# visited lines to detect it. Before executing each line, just see if we've been
# here before.
#
# Part 2 is more difficult. Somewhere in the program is either a JMP that should
# be a NOP, or a NOP that should be a JMP. Switching exactly one instruction
# will break the infinite loop and allow the program to finish. Manually
# debugging the assembly spaghetti is a non-starter, though I did look for
# anything obvious.
# Wrote an ugly brute-force solution with a bunch of redundant code.
################################################################################
import time

def runProg(instrs, pc, acc):
    visitedLines = set()
    while True:
        if pc in visitedLines:
            return 'LOOP', acc
        if pc >= len(instrs):
            return 'END', acc
        instr = instrs[pc].split(' ')[0]
        n = int(instrs[pc].split(' ')[1])
        visitedLines.add(pc)
        if instr == 'acc':
            acc += n
            pc += 1
        elif instr == 'jmp':
            pc += n
        else:
            pc += 1

#Entry point
start_time = time.time()

file=open('Input8.txt')
instrs = [line.strip() for line in file]
file.close()

pc = 0
acc = 0
visitedLines = set()
acc2 = 0
while True:
    if pc in visitedLines:
        break
    instr = instrs[pc].split(' ')[0]
    n = int(instrs[pc].split(' ')[1])
    visitedLines.add(pc)
    if instr == 'acc':
        acc += n
        pc += 1
    elif instr == 'jmp':
        t1, t2 = runProg(instrs, pc+1, acc)
        if t1 == 'END':
            acc2 = t2
        pc += n
    else:
        t1, t2 = runProg(instrs, pc+n, acc)
        if t1 == 'END':
            acc2 = t2
        pc += 1

print('Part 1:', acc)
print('Part 2:', acc2)

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
