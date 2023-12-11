
from functools import cmp_to_key

def hand_comparison_func(h1, h2):
    def num_matches(h, l):
        num_js = 0
        for card in h:
            match card:
                case 'A':
                    l[12] += 1
                case 'K':
                    l[11] += 1
                case 'Q':
                    l[10] += 1
                case 'J':
                    num_js += 1
                case 'T':
                    l[8] += 1
                case _:
                    l[int(card) - 2] += 1
        ## the highest value thing you can do with "floating" j's is 
        ## to add them to the highest concentration card
        l[l.index(max(l))] += num_js

    def points(l):
        if 5 in l:
            return 6
        if 4 in l:
            return 5
        if 3 in l and 2 in l:
            return 4
        if 3 in l:
            return 3
        if 2 in l:
            if l.count(2) == 2:
                return 2
            else:
                return 1
        return 0

    card_match1, card_match2 = [0] * 13, [0] * 13
    num_matches(h1,  card_match1)
    num_matches(h2, card_match2)
    if points(card_match1) < points(card_match2):
        return -1
    elif points(card_match2) < points(card_match1):
        return 1
    else:
        for c1, c2 in [(h1[i], h2[i]) for i in range(len(h1))]:
            match c1:
                case 'A':
                    x = 14
                case 'K':
                    x = 13
                case 'Q':
                    x = 12
                case 'J':
                    x = 1
                case 'T':
                    x = 10
                case _:
                    x = int(c1)
            match c2:
                case 'A':
                    y = 14
                case 'K':
                    y = 13
                case 'Q':
                    y = 12
                case 'J':
                    y = 1
                case 'T':
                    y = 10
                case _:
                    y = int(c2)
            if x < y:
                return -1
            elif x > y:
                return 1
        return 0

    
input_file  = "2023/d7/input.txt"

with open(input_file, "r") as input:
    data = input.readlines()

hands = [hand.split()[0] for hand in data]
bets = { hand.split()[0]: int(hand.split()[1]) for hand in data}

ranked_hands = sorted(hands, key=cmp_to_key(hand_comparison_func))

print("What are the total winnings?")
total_winnings = sum([bets[hand] * (ranked_hands.index(hand) + 1) for hand in ranked_hands])
print(total_winnings)
