
def next_node(i, j, blackMap, pipeMap):
    
    match (pipeMap[i][j]):

            case '|':
                if blackMap[max(i-1, 0)][j]:
                    i += 1
                else:
                    i -= 1
                
            case '-':
                if blackMap[i][max(j-1, 0)]:
                    j += 1 
                else:
                    j -= 1
                    
            case 'L':
                if blackMap[i][min(j+1, n-1)]:
                    i -= 1
                else:
                    j += 1

            case 'J':
                if blackMap[i][max(j-1, 0)]:
                    i -= 1
                else: 
                    j -= 1

            case '7':
                if blackMap[i][max(j-1, 0)]:
                    i += 1
                else: 
                    j -= 1

            case 'F':
                if blackMap[i][min(j+1, n-1)]:
                    i += 1 
                else:
                    j += 1
    return i, j



input_file = "input.txt"

# read in data as nested char array
with open(input_file, "r") as data:
    pipeMap = data.readlines()

pipeMap = [ [ letter for letter in line[:-1] ] for line in pipeMap ]
blackMap = [ [False for line in pipeLine] for pipeLine in pipeMap ]

m = len(pipeMap)
n = len(pipeMap[0])


start = [ [i, j] for i in range(len(pipeMap)) for j in range(len(pipeMap[0])) if pipeMap[i][j] == 'S' ][0]

fasti, fastj = start[0], start[1]

blackMap[fasti][fastj] = True

if fasti - 1 != -1 and not blackMap[fasti-1][fastj] and pipeMap[fasti-1][fastj] in ['|', 'F', '7']:
    fasti -= 1
elif fasti + 1 != m and not blackMap[fasti+1][fastj] and pipeMap[fasti+1][fastj] in ['|', 'L', 'J']:
    fasti += 1
elif fastj - 1 != -1 and not blackMap[fasti][fastj-1] and pipeMap[fasti][fastj-1] in ['-', 'F', 'L']:
    fastj -= 1
elif fastj + 1 != n and not blackMap[fasti][fastj+1] and pipeMap[fasti][fastj+1] in ['-', '7', 'J']:
    fastj += 1

i = 1
while fasti != start[0] or fastj != start[1]:

    i += 1
    blackMap[fasti][fastj] = True
    fasti, fastj = next_node(fasti, fastj, blackMap, pipeMap)

    if blackMap[fasti][fastj]:
        break

print("How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?")
print(int(i/2))