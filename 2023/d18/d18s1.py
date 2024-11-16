
input_file = "input.txt"
with open(input_file, "r") as data:
    digPlan = data.readlines()

# get list of all verticies
verticies = [(0,0)]
numBoundryPoints = 0
for step in digPlan:
    direction = step.split()[0]
    length = int(step.split()[1])
    numBoundryPoints += length
    match direction:
        case 'R':
            verticies.append((verticies[-1][0]+length, verticies[-1][1]))
        case 'L':
            verticies.append((verticies[-1][0]-length, verticies[-1][1]))
        case 'U':
            verticies.append((verticies[-1][0], verticies[-1][1]+length))
        case 'D':
            verticies.append((verticies[-1][0], verticies[-1][1]-length))

# shoelace formula to get area
area = int(abs(sum([(verticies[i][0]*verticies[i+1][1])-(verticies[i][1]*verticies[i+1][0]) for i in range(len(verticies)-1)]) / 2))

# Pick's Theorem to get internal points
numInternalPoints = area - int(numBoundryPoints/2) + 1

print("how many cubic meters of lava could it hold?")
print(numBoundryPoints + numInternalPoints)