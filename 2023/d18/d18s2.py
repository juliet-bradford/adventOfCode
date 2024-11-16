
input_file = "input.txt"
with open(input_file, "r") as data:
    digPlan = data.readlines()

digPlan = [line.split()[-1].strip("(#)") for line in digPlan]

# get list of all verticies
verticies = [(0,0)]
numBoundryPoints = 0
for step in digPlan:
    direction = int(step[-1])
    length = int(step[:-1], 16)
    numBoundryPoints += length
    # 0 == R | 1 == D | 2 == L | 3 == U
    match direction:
        case 0:
            verticies.append((verticies[-1][0]+length, verticies[-1][1]))
        case 2:
            verticies.append((verticies[-1][0]-length, verticies[-1][1]))
        case 3:
            verticies.append((verticies[-1][0], verticies[-1][1]+length))
        case 1:
            verticies.append((verticies[-1][0], verticies[-1][1]-length))

# shoelace formula to get area
area = int(abs(sum([(verticies[i][0]*verticies[i+1][1])-(verticies[i][1]*verticies[i+1][0]) for i in range(len(verticies)-1)]) / 2))

# Pick's Theorem to get internal points
numInternalPoints = area - int(numBoundryPoints/2) + 1

print("how many cubic meters of lava could it hold?")
print(numBoundryPoints + numInternalPoints)