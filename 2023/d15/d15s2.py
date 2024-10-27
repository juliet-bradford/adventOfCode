
def getHash(entry) -> int:
    currentValue = 0
    for letter in entry:
        currentValue = ((currentValue + ord(letter)) * 17) % 256
    return currentValue

input_file = "input.txt"

with open(input_file, "r") as data:
    entries = data.readlines()[0].strip('\n').split(',')

# make boxes
boxes = {i: [] for i in range(256)}

for entry in entries:
    # read data
    lensTag = entry.split('=')[0] if '=' in entry else entry.split('-')[0]
    boxNumber = getHash(lensTag)
    focalLength = int(entry.split('=')[1]) if '=' in entry else 0

    # if present, adjust, if not present add, if subtracting, find and remove
    if '=' in entry:
        alreadyPresent = False
        for i, lens in enumerate(boxes[boxNumber]):
            if lensTag == lens[0]:
                boxes[boxNumber][i][1] = focalLength
                alreadyPresent = True
        if not alreadyPresent:
            boxes[boxNumber].append([lensTag, focalLength])
    else:
        for lens in boxes[boxNumber]:
            if lensTag == lens[0]:
                boxes[boxNumber].remove(lens)
                break

focusingPower = 0
for box in boxes:
    for slot, lens in enumerate(boxes[box]):
        focusingPower += (box+1) * (slot+1) * lens[1]


print("What is the focusing power of the resulting lens configuration?", focusingPower)