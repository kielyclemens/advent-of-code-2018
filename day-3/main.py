import re

file = open("input.txt", "r")
lines = file.readlines()

claimsMap = {}
overlap = 0
for line in lines:
    nums = re.search(r'@ (\d+),(\d+): (\d+)x(\d+)', line)
    fromLeft = int(nums.group(1))
    fromTop = int(nums.group(2))
    width = int(nums.group(3))
    height = int(nums.group(4))
    for i in range(fromLeft, fromLeft+width):
        if i not in claimsMap:
            claimsMap[i] = {}
        for j in range(fromTop, fromTop+height):
            if j not in claimsMap[i]:
                claimsMap[i][j] = 1
            else:
                claimsMap[i][j] += 1

for i in claimsMap.values():
    for j in i.values():
        if j > 1:
            overlap += 1

part2Answer = -1
for line in lines:
    noOverlap = True
    nums = re.search(r'(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    id = int(nums.group(1))
    fromLeft = int(nums.group(2))
    fromTop = int(nums.group(3))
    width = int(nums.group(4))
    height = int(nums.group(5))
    for i in range(fromLeft, fromLeft+width):
        for j in range(fromTop, fromTop+height):
            if claimsMap[i][j] > 1:
                noOverlap = False
    if noOverlap:
        part2Answer = id

print("Part 1 answer: " + str(overlap))
print("Part 2 answer: " + str(part2Answer))