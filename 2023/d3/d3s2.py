
import re

input_file = "2023/d3/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

gear_ratio_sum = 0
gears = {}

upper_row = "." * (len(data[0]) - 1)

for idx, line in enumerate(data):
    lower_row = data[idx + 1] if idx != len(data) - 1 else "."  * (len(data[0]) - 1)
    current_row = line.strip("\n")

    matches = re.findall("[0-9]+", current_row)
    for match in matches:
        lower = min(abs(current_row.find(match) - 1), current_row.find(match))
        upper = min(len(current_row), current_row.find(match) + len(match) + 1)

        s = "\*"
        if re.search(s, current_row[lower:upper]):
            j = re.search(s, current_row[lower:upper]).span()[0] + lower
            if idx not in gears:
                gears[idx] = {}
            if j not in gears[idx]:
                gears[idx][j] = []
            gears[idx][j].append(match)
                
        if re.search(s, upper_row[lower:upper]):
            j = re.search(s, upper_row[lower:upper]).span()[0] + lower
            if idx - 1 not in gears:
                gears[idx - 1] = {}
            if j not in gears[idx - 1]:
                gears[idx - 1][j] = []
            gears[idx - 1][j].append(match)

        if re.search(s, lower_row[lower:upper]):
            j = re.search(s, lower_row[lower:upper]).span()[0] + lower
            if idx + 1 not in gears:
                gears[idx + 1] = {}
            if j not in gears[idx + 1]:
                gears[idx + 1][j] = []
            gears[idx + 1][j].append(match)

        current_row = current_row.replace(match, '.' * len(match),  1)
    upper_row = line

for x in gears:
    for y in gears[x]:
        if len(gears[x][y]) == 2:
            gear_ratio_sum += int(gears[x][y][0]) * int(gears[x][y][1])    

print("What is the sum of all of the gear ratios in your engine schematic?")
print(gear_ratio_sum)
