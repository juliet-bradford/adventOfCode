
def almanac_parse(data):
    mapping = {}
    line = next(data)
    while line != "\n":
        almanac_nums = [int(i) for i in line.split()]
        mapping[(almanac_nums[1], almanac_nums[1] + almanac_nums[2] - 1)] = almanac_nums[0] - almanac_nums[1]
        try:
            line = next(data)
        except StopIteration:
            return mapping
    try:
        next(data)
    except StopIteration:
        return mapping
    return mapping

def num_mapper(num, mapping):
    for map in list(mapping.keys()):
        if map[0] <= num and num <= map[1]:
            return num + mapping[map]
        
    return num

def map_clean(ranges):
    broke_early = True
    while broke_early:
        broke_early = False
        for i in range(len(ranges)):
            if i != len(ranges) - 1 and ranges[i][1] + 1 == ranges[i + 1][0]:
                ranges[i + 1] = (ranges[i][0], ranges[i + 1][1])
                ranges.pop(i)
                broke_early = True
                break
    return ranges

def mapper(ranges, mapping):
    ## put lower number where it should now go
    ## look at next number and find all mapping ranges between lower number and upper number
    ## fill in new tuples as needed, repeat

    mapped_ranges = []
    map_ranges = list(mapping.keys())
    
    while ranges:
        range = ranges[0]
        for key in map_ranges:
            ## if we are less than a range
            if range[0] < key[0]:
                if range[1] < key[0]:
                    mapped_ranges.append((range[0], range[1]))
                    ranges.pop(0)
                else:
                    mapped_ranges.append((range[0], key[0] - 1))
                    ranges[0] = (key[0], range[1])
                break
            ## if we are in a range
            if key[0] <= range[0] and range[0] <= key[1]:
                if range[1] <= key[1]:
                    new_range_start = min(num_mapper(range[0], mapping), num_mapper(range[1], mapping))
                    new_range_end = max(num_mapper(range[0], mapping), num_mapper(range[1], mapping))
                    mapped_ranges.append((new_range_start, new_range_end))
                    ranges.pop(0)
                else:
                    new_range_start = min(num_mapper(range[0], mapping), num_mapper(key[1], mapping))
                    new_range_end = max(num_mapper(range[0], mapping), num_mapper(key[1], mapping))
                    mapped_ranges.append((new_range_start, new_range_end))
                    ranges[0] = (key[1] + 1, range[1])
                break
        ## if all remaining ranges are above final mapping range
        if range[0] > map_ranges[-1][1]:
            while ranges:
                mapped_ranges.append((ranges[0][0], ranges[0][1]))
                ranges.pop(0)
                
    return map_clean(sorted(mapped_ranges))


input_file = "2023/d5/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

seeds = [int(i) for i in data[0].split()[1:]]
seeds = sorted([(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds) - 1, 2)])

# map upper and lower values to offset from destination
data = iter(data[3:])

seed_to_soil = dict(sorted(almanac_parse(data).items()))
soil_to_fertilizer = dict(sorted(almanac_parse(data).items()))
fertilizer_to_water = dict(sorted(almanac_parse(data).items()))
water_to_light = dict(sorted(almanac_parse(data).items()))
light_to_temperature = dict(sorted(almanac_parse(data).items()))
temperature_to_humidity = dict(sorted(almanac_parse(data).items()))
humidity_to_location = dict(sorted(almanac_parse(data).items()))


mapped_ranges = mapper(mapper(mapper(mapper(mapper(mapper(mapper(seeds, 
                                                                seed_to_soil), 
                                                                soil_to_fertilizer), 
                                                                fertilizer_to_water), 
                                                                water_to_light), 
                                                                light_to_temperature), 
                                                                temperature_to_humidity), 
                                                                humidity_to_location)



print("What is the lowest location number that corresponds to any of the initial seed numbers?")
print(mapped_ranges[0][0])