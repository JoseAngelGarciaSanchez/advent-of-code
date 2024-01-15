import os


def compute_rock_loads(file_path: str | os.PathLike) -> int:
    """"""
    input_file = open(file_path, "r")
    space = input_file.readlines()
    space = [[line.strip()] for line in space]
    print(space)

    return 0, 0


def _rotation(direction):
    pass


if __name__ == "__main__":
    day1_file_path = "./../../data/day14.txt"
    first_part, second_part = compute_rock_loads(day1_file_path)
    print(f"The answer for the first part is: {first_part}")
    print(f"The answer for the second part is {second_part}")