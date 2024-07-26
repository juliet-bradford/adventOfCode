
input_file = "input.txt"

with open(input_file, "r") as data:
    spaceMap = data.readlines()


m = len(spaceMap)
n = len(spaceMap[0]) - 1


# adding space dilation
i = 0
while i < m:
    if spaceMap[i].count('#') == 0:
        spaceMap.insert(i, ('.'*n)+'\n')
        i += 1
        m += 1
    i += 1

j = 0
while j < n:
    if [spaceMap[i][j] for i in range(m)].count('#') == 0:
        for i in range(m):
            spaceMap[i] = spaceMap[i][:j] + '.' + spaceMap[i][j:]
        j += 1
        n += 1
    j += 1


# get galaxy coords
galaxyCoords = []
for i in range(m):
    for j in range(n):
        if spaceMap[i][j] == '#':
            galaxyCoords.append([i, j])


# sum all distances
distSum = 0
for i in range(len(galaxyCoords)):
    for j in range(i+1, len(galaxyCoords)):
        distSum += abs(galaxyCoords[i][0] - galaxyCoords[j][0]) + abs(galaxyCoords[i][1] - galaxyCoords[j][1])

print("What is the sum of these lengths?")
print(distSum)