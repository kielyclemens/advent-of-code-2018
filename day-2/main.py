import re

file = open("input.txt", "r")
lines = file.readlines()

twoCount = 0
threeCount = 0
prevIDs = []
matches = []

part2solution = ""
for line in lines:
    line = line[:len(line)-1]
    letterCount = {}
    for char in line:
        if char in letterCount:
            letterCount[char] += 1
        else:
            letterCount[char] = 1
    two = False
    three = False
    for k, v in letterCount.items():
        if v == 2:
            two = True
        elif v == 3:
            three = True
    if two:
        twoCount += 1
    if three:
        threeCount += 1

    for prevID in prevIDs:
        diffSeen = False
        match = True
        for x in range(len(line)):
            if line[x] != prevID[x]:
                if diffSeen:
                    match = False
                else:
                    diffSeen = True
        if match:
            matches = [prevID, line]
    prevIDs.append(line)

for x in range(len(matches[0])):
    if matches[0][x] == matches[1][x]:
        part2solution += matches[0][x]

print("Part 1 answer: " + str(twoCount*threeCount))
print("Part 2 answer: " + part2solution)