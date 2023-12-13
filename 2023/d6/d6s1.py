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

times = [int(i) for i in data[0].split()[1:]]
distances = [int(i) for i in data[1].split()[1:]]
winners = [numbers_of_winners(times[i], distances[i]) for i in range(len(times))]
winners_product = reduce((lambda x,y: x * y), winners)


print("What do you get if you multiply these numbers together?")
print(winners_product)