import re  

input_file = "2023/d2/input.txt"

with open(input_file, "r") as data:
    games = data.readlines()

game_min_amounts = []

for game in games:
    red, blue, green = 1, 1, 1

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
                    if amount > red:
                        red = amount

                case "blue":
                    if amount > blue:
                        blue = amount

                case "green":
                    if amount > green:
                        green = amount

    game_min_amounts.append((red, blue, green))
    
sum_of_game_powers = 0
for game in game_min_amounts:
    sum_of_game_powers += game[0] * game[1] * game[2]


print("What is the sum of the power of these sets?")
print(sum_of_game_powers)