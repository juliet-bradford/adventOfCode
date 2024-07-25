
input_file = "test.txt"

with open(input_file, "r") as data:
    spaceMap = data.readlines()


m = len(spaceMap)
n = len(spaceMap[0]) - 1

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


galaxyCoords = []
for i in range(m):
    for j in range(n):
        print(spaceMap[i][j],end='')
    print('')

