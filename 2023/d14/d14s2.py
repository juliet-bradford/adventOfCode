
def rotateClockwise(platform: list[str]) -> list[str]:
    rotatedPlatform = ["" for i in platform[0]]
    for row in reversed(platform):
        for i in range(len(row)):
            rotatedPlatform[i] += row[i]

    return rotatedPlatform

def rotateCounterClockwise(platform) -> list[str]:
    rotatedPlatform = rotateClockwise(platform)
    rotatedPlatform = rotateClockwise(rotatedPlatform)
    rotatedPlatform = rotateClockwise(rotatedPlatform)
    return rotatedPlatform

def printPlatform(platform: list[str]):
    for row in platform:
        print(row)
    print('')

input_file = "input.txt"

with open(input_file, "r") as data:
    platform = data.readlines()
    platform = [row.strip('\n') for row in platform]


# rotate so that left is aligned with north
platform = rotateCounterClockwise(platform)
#slide rocks left
platform = ['#'.join([''.join(sorted(substr, reverse=True)) for substr in row.split('#')]) for row in platform]
count = 1

seenPlatforms = {}
while tuple(platform) not in seenPlatforms.keys():
    # add to seen platforms
    seenPlatforms[tuple(platform)] = count
    # rotate clockwise
    platform = rotateClockwise(platform)
    # slide rocks left
    platform = ['#'.join([''.join(sorted(substr, reverse=True)) for substr in row.split('#')]) for row in platform]

    count += 1

numRotationsBeforeCycle = seenPlatforms[tuple(platform)]
numRotationsInCycle = count - numRotationsBeforeCycle

# get where in cycle rotation ends (left guaranteed aligned with east)
rotations = ((4000000000 - numRotationsBeforeCycle) % numRotationsInCycle) + numRotationsBeforeCycle
inverseSeenPlatforms = {v: k for k, v in seenPlatforms.items()}
platform = inverseSeenPlatforms[rotations]

# left is aligned with east, so do two rotations to align it with west (so north is up)
platform = rotateClockwise(platform)
platform = rotateClockwise(platform)

# add rocks up
totalLoad = 0
for i in range(len(platform)):
    totalLoad += platform[i].count('O') * (len(platform) - i)

print("what is the total load on the north support beams?", totalLoad)