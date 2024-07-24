
input_file = "2023/d9/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

data = [[int(i) for i in line.split()] for line in data]

pre_value_sum = 0

for value_history in data:
    first_values = []
    while any(value_history):
        first_values.append(value_history[0])
        value_history = [value_history[i] - value_history[i - 1] for i in range(1, len(value_history))]
    pre_value = first_values[-1]
    for val in first_values[-2::-1]:
        pre_value = val - pre_value
    pre_value_sum  += pre_value

print("What is the sum of these extrapolated values?")
print(pre_value_sum)