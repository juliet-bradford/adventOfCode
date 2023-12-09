
import re

input_file = "2023/d3/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

part_numbers_sum = 0

## list of all indicies on that row touching a symbol 
upper_row = "." * (len(data[0]) - 1)

for idx, line in enumerate(data):
    lower_row = data[idx + 1] if idx != len(data) - 1 else "."  * (len(data[0]) - 1)
    current_row = line.strip("\n")

    matches = re.findall("[0-9]+", current_row)
    for match in matches:
        lower = min(abs(current_row.find(match) - 1), current_row.find(match))
        upper = min(len(current_row), current_row.find(match) + len(match) + 1)
        #print(match + " " + str(lower) + " " + str(upper))

        s = "[\-\$\+\*\/#@=%&]"
        if re.search(s, current_row[lower:upper]) or re.search(s, upper_row[lower:upper]) or re.search(s, lower_row[lower:upper]):
            #print("part_numbers_sum = " + str(part_numbers_sum) + " + " + match)
            part_numbers_sum += int(match)

        current_row = current_row.replace(match, '.' * len(match),  1)
    upper_row = line
    

print("What is the sum of all of the part numbers in the engine schematic?")
print(part_numbers_sum)

if part_numbers_sum < 554988:
    print("Too low, less than " + str(554988))