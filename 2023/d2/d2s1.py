import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

## start by parsing games

input_file = "2023/d2/input.txt"

with open(input_file, "r") as data:
    games = data.readlines()

sum_of_possible_game_IDs = 0

for game in games:

    possible = True

    game = game.lstrip("Game ")
    game_ID = re.search('\d+', game).group()
    game = game.lstrip(game_ID + ":")
    game = game.rstrip("\n")

    game = game.split(";")
    for round in game:
        cube_amount_color = round.split(",")
        for amount_color in cube_amount_color:
            amount_color = amount_color.lstrip(" ")
            amount_color = amount_color.split(" ")

            amount = int(amount_color[0])
            color = amount_color[1]
            match color:
                case "red":
                    if amount > MAX_RED:
                        possible = False

                case "blue":
                    if amount > MAX_BLUE:
                        possible = False

                case "green":
                    if amount > MAX_GREEN:
                        possible = False

    if possible:
        sum_of_possible_game_IDs += int(game_ID)

print("What is the sum of the IDs of those games?")
print(sum_of_possible_game_IDs)