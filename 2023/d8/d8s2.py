
import re
from math import lcm
from functools import reduce

## from reddit:
## The input for part 2 was constructed very nicely so that each cycle
## hits 'Z' at every multiple of the cycle length
## 
## ...
## well that makes the problem a whole lot easier

input_file = "2023/d8/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

navigation_instructions = data[0].strip('\n')
network_info = {re.findall('[A-Z0-9]+', rule)[0] :  (re.findall('[A-Z0-9]+', rule)[1], re.findall('[A-Z0-9]+', rule)[2]) for rule in data[2:]}

starting_locations = [node for node in network_info.keys() if node[2] == 'A']

cycle_lengths = []
for path in starting_locations:
    copy = path
    steps = 0
    while copy[2] != 'Z':
        for instruction in navigation_instructions:
            steps += 1
            if copy[2] == 'Z':
                break
            copy = network_info[copy][0] if instruction ==  'L' else network_info[copy][1]
    
    cycle_lengths.append(steps)

steps_taken = reduce(lcm, cycle_lengths)

print("How many steps are required to reach ZZZ?")
print(steps_taken)