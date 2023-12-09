
def total_scratches_generated(card, scratchoffs, scratches_generated_by_card):
    if card in scratches_generated_by_card:
        return scratches_generated_by_card[card]
    else:
        winning_nums = [int(i) for i in scratchoffs[card].split("|")[0].split()[2:]]
        our_nums = [int(i) for i in scratchoffs[card].split("|")[1].split()]
        scratches_generated_by_card[card] = len(set(winning_nums) & set(our_nums))

        for i in range(card + 1, card + scratches_generated_by_card[card] + 1):
            scratches_generated_by_card[card] += total_scratches_generated(i, scratchoffs, scratches_generated_by_card)
        return scratches_generated_by_card[card]


input_file = "2023/d4/input.txt"

with open(input_file, "r") as data:
    scratchoffs = data.readlines()

total_scratchoffs = 0
scratches_generated_by_card = {}

for i in range(len(scratchoffs)):
    total_scratchoffs += total_scratches_generated(i, scratchoffs, scratches_generated_by_card) + 1

print("how many total scratchcards do you end up with?")
print(total_scratchoffs)