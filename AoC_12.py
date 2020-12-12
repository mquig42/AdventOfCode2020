################################################################################
# 2020-12-12
# Advent of Code 2020 Day 12
# Mike Quigley
#
# Interpret ship navigation directions. All turns are multiples of 90 degrees.
# For my coordinate system, North and East are positive,
# South and West are negative
#
# All turns being multiples of 90 degrees makes this easy. There are only 4
# possible headings in part 1, and 3 possible rotations in part 2. This means
# that there is no need for trigonometry.
################################################################################
import time

#Given the input as a list of strings, solve part 1
def solve1(directions):
    nspos = 0       #North-South position
    ewpos = 0       #East-West position
    heading = 90    #Heading
    
    for line in directions:
        if line[0] == 'N' or (heading == 0 and line[0] == 'F'):
            nspos += int(line[1:])
        elif line[0] == 'S' or (heading == 180 and line[0] == 'F'):
            nspos -= int(line[1:])
        elif line[0] == 'E' or (heading == 90 and line[0] == 'F'):
            ewpos += int(line[1:])
        elif line[0] == 'W' or (heading == 270 and line[0] == 'F'):
            ewpos -= int(line[1:])
        elif line[0] == 'L':
            heading = (heading - int(line[1:])) % 360
        elif line[0] == 'R':
            heading = (heading + int(line[1:])) % 360
    return abs(nspos) + abs(ewpos)

#Now solve part 2
def solve2(directions):
    n = 0       #North
    e = 0       #East
    wpn = 1     #Waypoint North
    wpe = 10    #Waypoint East

    for line in directions:
        if line[0] == 'N':
            wpn += int(line[1:])
        elif line[0] == 'S':
            wpn -= int(line[1:])
        elif line[0] == 'E':
            wpe += int(line[1:])
        elif line[0] == 'W':
            wpe -= int(line[1:])
        elif line[0] == 'F':
            for i in range(int(line[1:])):
                n += wpn
                e += wpe
        elif line == 'L90' or line == 'R270':
            #Left 90 rotation
            tmp = wpe
            wpe = wpn * -1
            wpn = tmp
        elif line == 'L180' or line == 'R180':
            #180 rotation
            wpe = wpe * -1
            wpn = wpn * -1
        elif line == 'L270' or line == 'R90':
            #Right 90 rotation
            tmp = wpe
            wpe = wpn
            wpn = tmp * -1

    return abs(n) + abs(e)

#Entry point
start_time = time.time()

file = open('Input12.txt')
directions = [line.strip() for line in file]
file.close()
    

print('Part 1:', solve1(directions))
print('Part 2:', solve2(directions))

print('Elapsed Time:', '{0:0.3f}s'.format(time.time() - start_time))
