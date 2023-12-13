from math import sqrt, ceil, floor
from functools import reduce

# d = (t - v) * v = tv - v^2
# so then -v^2 + tv - d = 0
# and by the quadratic formula
# v = (-t +- sqrt(t^2 - 4(-1)(-d))) / 2(-1)
#   = (t +- sqrt(t^2 - 4d)) / 2

def numbers_of_winners(t, d):
    return ceil((t + sqrt(t**2 - 4*d))/2) - floor((t - sqrt(t**2 - 4*d))/2) - 1

input_file = "2023/d6/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

time = int(data[0].split(':')[1].replace(" ", ""))
distance = int(data[1].split(':')[1].replace(" ", ""))
winner = numbers_of_winners(time, distance)


print("How many ways can you beat the record in this one much longer race?")
print(winner)