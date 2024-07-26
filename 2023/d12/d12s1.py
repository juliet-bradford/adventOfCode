
from re import sub

def numberOfArrangements (springs: str, groupLengths, currentGroupLength):
    
    if len(springs) == 0 and (len(groupLengths) != 1 or currentGroupLength != groupLengths[0]):
        return 0 

    arraSum = 0

    # if we have no group yet
    if currentGroupLength == 0:
        if springs[0] == '.':
            arraSum += numberOfArrangements(springs[1:], groupLengths, currentGroupLength)
        elif springs[0] == '#':
            arraSum += numberOfArrangements(springs[1:], groupLengths, 1)
        else:
            arraSum += numberOfArrangements(springs[1:], groupLengths, currentGroupLength)
            arraSum += numberOfArrangements(springs[1:], groupLengths, 1)


    # if our group is not done yet
    elif currentGroupLength < groupLengths[0]:
        if springs[0] == '.':
            return 0
        else:
            arraSum += numberOfArrangements(springs[1:], groupLengths, currentGroupLength+1)

    # if we have completed our group
    else:
        # if we are at the end, validity test and return
        if len(groupLengths) == 1:
            return 1 if springs.count('#') == 0 else 0
        
        # if next is '#' then we fucked up
        if springs[0] == '#':
            return 0
        # if next is '?' we have to treat it as '.', and start new group
        else:
            arraSum += numberOfArrangements(springs[1:], groupLengths[1:], 0)

    return arraSum


input_file = "input.txt"

with open(input_file, "r") as data:
    damagedRecords = data.readlines()

groupLengthsList = [[int(num) for num in record.split(' ')[1].strip('\n').split(',')] for record in damagedRecords]
springsList = [sub('\.\.+','.', record.split(' ')[0].strip('.')) for record in damagedRecords]

# try some backtracking
sumOfArrangements = 0
for springs, groupLengths in zip(springsList, groupLengthsList):
    sumOfArrangements += numberOfArrangements(springs, groupLengths, 0)

print("What is the sum of those counts?")
print(sumOfArrangements)