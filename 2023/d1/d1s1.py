
## run from adventOfCode directory
puzzle_input = "./2023/d1/input.txt"
sum = 0

with open(puzzle_input, "r") as input:
    calibration_document = input.readlines()

for line in calibration_document:
    first_digit = int(next((x for x in line if x.isnumeric()), 0))
    line = line[::-1]
    second_digit = int(next((x for x in line if x.isnumeric()), 0))
    sum += first_digit * 10 + second_digit

print("What is the sum of all of the calibration values? " + str(sum))