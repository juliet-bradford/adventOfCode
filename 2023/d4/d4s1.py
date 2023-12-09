
input_file = "2023/d4/input.txt"

with open(input_file, "r") as data:
    scratchoffs = data.readlines()

point_sum = 0

for scratch in scratchoffs:
    winning_nums = [int(i) for i in scratch.split("|")[0].split()[2:]]
    our_nums = [int(i) for i in scratch.split("|")[1].split()]

    matches = len(set(winning_nums) & set(our_nums))
    point_sum += 2**(matches  - 1) if matches != 0 else 0

print("How many points are they worth in total?")
print(point_sum)