
input_file = "input.txt"

with open(input_file, "r") as data:
    entries = data.readlines()[0].strip('\n').split(',')

hashSum = 0
for entry in entries:
    currentValue = 0
    for letter in entry:
        currentValue = ((currentValue + ord(letter)) * 17) % 256
    hashSum += currentValue

print("Hash Sum: ", hashSum)