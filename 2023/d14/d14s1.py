
input_file = "input.txt"

with open(input_file, "r") as data:
    lines = data.readlines()
    for line in lines:
        print(line, end='')
    print('')

    cols = [ ''.join([lines[j][k] for j in range(len(lines))]) for k in range(len(lines[0]))][:-1]


newCols = []
for t, col in enumerate(cols):
    
    slidCol = []
    for split in col.split('#'):
        slidCol.append(''.join(sorted(split, reverse=True)))

    newCols.append('#'.join(slidCol))

totalLoad = sum([sum([len(col)-i for i in range(len(col)) if col[i] == 'O']) for col in newCols])

print("what is the total load on the north support beams?")
print(totalLoad)