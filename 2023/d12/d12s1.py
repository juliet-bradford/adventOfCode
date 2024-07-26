def isValid (dRec, cRec):
    return [len(i) for i in dRec.split('.') if i != ''] == cRec
    


def numberOfArrangements (dRec: str, cRec):
    arraSum = 0

    if dRec.count('?') == 0:
        return 1 if isValid(dRec, cRec) else 0
    
    arraSum += numberOfArrangements(dRec.replace('?', '#', 1), cRec)
    arraSum += numberOfArrangements(dRec.replace('?', '.', 1), cRec)

    return arraSum


input_file = "input.txt"

with open(input_file, "r") as data:
    damagedRecords = data.readlines()

contiguousRecords = [[int(num) for num in record.split(' ')[1].strip('\n').split(',')] for record in damagedRecords]
damagedRecords = [record.split(' ')[0] for record in damagedRecords]

# try some backtracking
sumOfArrangements = 0
for dRec, cRec in zip(damagedRecords, contiguousRecords):
    sumOfArrangements += numberOfArrangements(dRec, cRec)

print("What is the sum of those counts?")
print(sumOfArrangements)