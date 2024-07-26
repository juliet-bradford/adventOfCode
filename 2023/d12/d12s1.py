
input_file = "test.txt"

with open(input_file, "r") as data:
    damagedRecords = data.readlines()

contiguousRecords = [[int(num) for num in record.split(' ')[1].strip('\n').split(',')] for record in damagedRecords]
damagedRecords = [record.split(' ')[0] for record in damagedRecords]

for i in damagedRecords:
    print(i)
for i in contiguousRecords:
    print(i)