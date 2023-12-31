
## make an altered prefix tree from each spelled out digit to search through line

## the examples did not make this clear but the number generated by "threeight" is 38,
## i.e. the same base string is read once forwards and once "backwards"

class Trie:
    def __init__(self) -> None:
        self.letters = {}
        self.num = 0

    def add_spelled_digit(self, digit, num):
        node = self
        for char in digit:
            if char not in node.letters:
                node.letters[char] = Trie()
            node = node.letters[char]
        node.num = num

    def in_tree(self, word):
        node = self
        for char in word:
            if node.num != 0:
                return node.num
            if char not in node.letters:
                return 0
            node = node.letters[char]
        return node.num


## run from adventOfCode directory
puzzle_input = "./2023/d1/input.txt"
sum = 0
spelled_out_digits = ["one", "two", "three", "four", "five", "six", "seven",  "eight", "nine"]

trie = Trie()
for digit in spelled_out_digits:
    trie.add_spelled_digit(digit, spelled_out_digits.index(digit) + 1)

rtrie = Trie()
for digit in spelled_out_digits:
    rtrie.add_spelled_digit(digit[::-1], spelled_out_digits.index(digit) + 1)

with open(puzzle_input, "r") as input:
    calibration_document = input.readlines()

for line in calibration_document:
    for i in range(len(line)):
        if line[i].isnumeric():
            first_digit = int(line[i])
            break
        num = trie.in_tree(line[i:])
        if num != 0:
            first_digit = num
            break

    line = line[::-1]
    for i in range(len(line)):
        if line[i].isnumeric():
            second_digit = int(line[i])
            break
        num = rtrie.in_tree(line[i:])
        if num != 0:
            second_digit = num
            break

    sum += first_digit * 10 + second_digit

print("What is the sum of all of the calibration values? " + str(sum))