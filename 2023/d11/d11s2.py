
input_file = "input.txt"

with open(input_file, "r") as data:
    spaceMap = data.readlines()


m = len(spaceMap)
n = len(spaceMap[0]) - 1


# finding space dilation rows and coloumns
dilationRows = []
for i, row in enumerate(spaceMap):
    if row.count('#') == 0:
        dilationRows.append(i)

dilationCols = []
j = 0
while j < n:
    if [spaceMap[i][j] for i in range(m)].count('#') == 0:
        dilationCols.append(j)
    j += 1


dilationConstant = 999999

# get galaxy coords
galaxyCoords = []
for i in range(m):
    for j in range(n):
        if spaceMap[i][j] == '#':
            galaxyCoords.append(
                [i + sum([dilationConstant for k in dilationRows if k < i]), 
                 j + sum([dilationConstant for k in dilationCols if k < j])])


# sum all distances
distSum = 0
for i in range(len(galaxyCoords)):
    for j in range(i+1, len(galaxyCoords)):
        distSum += abs(galaxyCoords[i][0] - galaxyCoords[j][0]) + abs(galaxyCoords[i][1] - galaxyCoords[j][1])

print("What is the sum of these lengths?")
print(distSum)