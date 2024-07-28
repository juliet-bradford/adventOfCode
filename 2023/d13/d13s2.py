def isOffByOne(p1, p2):
    offBy = 0
    p1 = ''.join(p1)
    p2 = ''.join(p2)
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            offBy += 1
        if offBy > 1:
            return False
        
    return False if offBy == 0 else True

def findReflectionPoint(pattern):
    patternLength = len(pattern)
    
    for i in range(patternLength-1):
        dist = min(i, patternLength-i-2)

        if isOffByOne(list(reversed(pattern[i-dist:i+1])), pattern[i+1:i+dist+2]):
            return i+1

    return 0

input_file = 'input.txt'

patternList = [[]]
patternListCols = []
with open(input_file, "r") as data:
    lines = data.readlines()

    i = 0
    for line in lines:
        if line == '\n':
            patternList.append([])
            patternListCols.append([ ''.join([patternList[i][j][k] for j in range(len(patternList[i]))]) for k in range(len(patternList[i][0]))])
            i += 1
        else:
            patternList[i].append(line.strip('\n'))
    patternListCols.append([ ''.join([patternList[i][j][k] for j in range(len(patternList[i]))]) for k in range(len(patternList[i][0]))])


summerize = 0

# do rows first
for pattern in patternList:
    summerize += findReflectionPoint(pattern) * 100

# now do coloumns
for pattern in patternListCols:
    summerize += findReflectionPoint(pattern)

print("What number do you get after summarizing all of your notes?")
print(summerize)