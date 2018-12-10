file = open("input.txt", "r")
lines = file.readlines()

finalFreq = 0
curFreq = 0
firstRepeat = -1
reachedFreqs = {}

reachedFreqs[0] = True

solution1 = False
solution2 = False

while solution2 is False:
    for line in lines:
        change = int(line)
        if solution1 is False:
            finalFreq += change
        curFreq += change
        if solution2 is False and curFreq in reachedFreqs:
            solution2 = True
            firstRepeat = curFreq
        elif solution2 is False:
            reachedFreqs[curFreq] = True

    solution1 = True

print("Part 1 answer: " + str(finalFreq))
print("Part 2 answer: " + str(firstRepeat))