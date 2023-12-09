
import bisect

def almanac_parse(data):
    mapping = {}
    line = next(data)
    while line != "\n":
        almanac_nums = [int(i) for i in line.split()]
        mapping[almanac_nums[1]] = almanac_nums[0] - almanac_nums[1]
        mapping[almanac_nums[1] + almanac_nums[2] - 1] = almanac_nums[0] - almanac_nums[1]
        try:
            line = next(data)
        except StopIteration:
            return mapping
    try:
        next(data)
    except StopIteration:
        return mapping
    return mapping

def mapper(num, mapping):
    if num in mapping:
        return num + mapping[num]
    
    idx = bisect.bisect_left(list(mapping.keys()), num)
    try:
        if mapping[list(mapping.keys())[idx - 1]] == mapping[list(mapping.keys())[idx]]:
            return num + mapping[list(mapping.keys())[idx]]
        else:
            return num
    except IndexError:
        return num

input_file = "2023/d5/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

seeds = [int(i) for i in data[0].split()[1:]]

# map upper and lower values to offset from destination
data = iter(data[3:])

seed_to_soil = dict(sorted(almanac_parse(data).items()))
soil_to_fertilizer = dict(sorted(almanac_parse(data).items()))
fertilizer_to_water = dict(sorted(almanac_parse(data).items()))
water_to_light = dict(sorted(almanac_parse(data).items()))
light_to_temperature = dict(sorted(almanac_parse(data).items()))
temperature_to_humidity = dict(sorted(almanac_parse(data).items()))
humidity_to_location = dict(sorted(almanac_parse(data).items()))


locations = [mapper(mapper(mapper(mapper(mapper(mapper(mapper(seed, 
                                                            seed_to_soil), 
                                                            soil_to_fertilizer), 
                                                            fertilizer_to_water), 
                                                            water_to_light), 
                                                            light_to_temperature), 
                                                            temperature_to_humidity), 
                                                            humidity_to_location)
for seed in seeds]

lowest_location = min(locations)

print("What is the lowest location number that corresponds to any of the initial seed numbers?")
print(lowest_location)