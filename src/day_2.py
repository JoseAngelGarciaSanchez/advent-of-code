import os
import re


def possibles_games(input_path: str | os.PathLike) -> list[int]:
    with open(input_path, "r") as file:
        games = file.readlines()

    games_input = [game.strip() for game in games]

    analysed_games = []

    for game in games_input:
        game_analyse = _analyse_game(game)

        analysed_games.append(game_analyse)

    total_sum = 0

    for game_analyse in analysed_games:
        if game_analyse["possible"]:
            number_str = re.findall(r"\d+", game["number"])
            total_sum += int(number_str[0])

    total_power = 0
    for game in games:
        total_power += game["power"]

    return total_sum, total_power


def _analyse_game(game):
    game_dict = {}

    colors_max = {"green": 13, "red": 12, "blue": 14}

    splitted = re.split(r":|;", game)

    game_dict["game_number"] = splitted[0]
    game_dict["possible"] = True

    min_required_blue = 0
    min_required_red = 0
    min_required_green = 0

    for i in range(1, len(splitted)):
        round = splitted[i].split(",")

        blue_number = None
        green_number = None
        red_number = None

        for color in round:
            blue = re.search(r"blue", color)
            green = re.search(r"green", color)
            red = re.search(r"red", color)

            if blue:
                blue_number = int(re.findall(r"\d+", color)[0])

                if min_required_blue < blue_number:
                    min_required_blue = blue_number

                if blue_number > colors_max["blue"]:
                    game_dict["possible"] = False
            if green:
                green_number = int(re.findall(r"\d+", color)[0])

                if min_required_green < green_number:
                    min_required_green = green_number

                if green_number > colors_max["green"]:
                    game_dict["possible"] = False
            if red:
                red_number = int(re.findall(r"\d+", color)[0])

                if min_required_red < red_number:
                    min_required_red = red_number

                if red_number > colors_max["red"]:
                    game_dict["possible"] = False

    game_dict["power"] = min_required_blue * min_required_green * min_required_red

    return game_dict
