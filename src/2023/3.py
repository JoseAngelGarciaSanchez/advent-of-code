import os

import numpy as np


def part_numbers(file_path: str | os.PathLike):
    with open(file_path, "r") as input_file:
        array = [list(line.strip()) for line in input_file]


if __name__ == "__main__":
    day3_file_path = "./../../data/day3.txt"
    with open(day3_file_path, "r") as file:
        data = file.read().split("\n\n")

    arr = []
    for line in data:
        arr.append([*line.strip()])

    print(np.array(arr))
