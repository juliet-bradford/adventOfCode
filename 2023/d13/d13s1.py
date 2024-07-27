
input_file = 'test0.txt'

patternList = [[]]
with open(input_file, "r") as data:
    lines = data.readlines()
    
    i = 0
    for line in lines:
        patternList[i].append(line.strip('\n'))
        if line == '\n':
            i += 1
            patternList.append([])


for pattern in patternList:
    for line in pattern:
        print(line)
    print('')

