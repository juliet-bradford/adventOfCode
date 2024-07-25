
from numpy.linalg import det

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


start = [ [i, j] for i in range(len(pipeMap)) for j in range(len(pipeMap[0])) if pipeMap[i][j] == 'S' ]
start = start[0]

fasti, fastj = start[0], start[1]

blackMap[fasti][fastj] = True

if not blackMap[max(fasti-1, 0)][fastj] and pipeMap[fasti-1][fastj] in ['|', 'F', '7']:
    fasti -= 1
elif not blackMap[min(fasti+1, m-1)][fastj] and pipeMap[fasti+1][fastj] in ['|', 'L', 'J']:
    fasti += 1
elif not blackMap[fasti][max(fastj-1)] and pipeMap[fasti][fastj-1] in ['-', 'F', 'L']:
    fastj -= 1
elif not blackMap[fasti][min(fastj+1, n-1)] and pipeMap[fasti][fastj+1] in ['-', '7', 'J']:
    fastj += 1

pipeLength = 1
pipe = [start]
while fasti != start[0] or fastj != start[1]:

    pipeLength += 1
    blackMap[fasti][fastj] = True
    pipe.append([fasti, fastj])
    fasti, fastj = next_node(fasti, fastj, blackMap, pipeMap)

    if blackMap[fasti][fastj]:
        break


# Pick's Formula: A = i + b/2 - 1 -> i = A + 1 - b/2
# for the area of a polygon with integer vertecies
#   i = number of interior points
#   b = number of boundry points


# Shoelace Formula: 
# 2A = | x1 x2 | + | x2 x3 | + ... + | xn x1 |
#      | y1 y2 | + | y2 y3 |         | yn y1 |

area = 0
for i in range(len(pipe)):
    area += det([pipe[i], pipe[(i+1)%len(pipe)]])

area = abs(int(area/2))
interior_points = area + 1 - int(pipeLength/2)


print("How many tiles are enclosed by the loop?")
print(int(interior_points))