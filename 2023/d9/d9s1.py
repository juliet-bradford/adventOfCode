
input_file = "2023/d9/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

data = [[int(i) for i in line.split()] for line in data]
next_value_sum = 0

for value_history in data:
    while any(value_history):
        next_value_sum += value_history[-1]
        value_history = [value_history[i] - value_history[i - 1] for i in range(1, len(value_history))]

print("What is the sum of these extrapolated values?")
print(next_value_sum)