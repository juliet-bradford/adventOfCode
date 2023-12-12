
import re

input_file = "2023/d8/test2.txt"

with open(input_file, "r") as input:
    data = input.readlines()

navigation_instructions = data[0].strip('\n')
network_info = {re.findall('[A-Z]+', rule)[0] :  (re.findall('[A-Z]+', rule)[1], re.findall('[A-Z]+', rule)[2]) for rule in data[2:]}

steps_taken = 0
current_location = 'AAA'
while current_location != 'ZZZ':
    for instruction in navigation_instructions:
        current_location = network_info[current_location][0] if instruction ==  'L' else network_info[current_location][1]
        steps_taken += 1
        if current_location == 'ZZZ':
            break

print("How many steps are required to reach ZZZ?")
print(steps_taken)