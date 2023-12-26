"""
This is the solution of the first day of advent of code
"""
import os
import re


number_list = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def number_extraction(file_path: str | os.PathLike) -> int:
    """
    First part of the day 1, 2023 AoC :)

    Extract and compute the sum of all numbers in a string.
    For the first part, only digits. For the second part
    digits and string numbers
    """
    input_file = open(file_path, "r")

    first_extraction = 0
    second_extraction = 0

    for line in input_file:
        first_extraction += _string_to_first_last_num(line, only_digits=True)
        second_extraction += _string_to_first_last_num(line, only_digits=False)

    return first_extraction, second_extraction


def _string_to_first_last_num(input_line: str, only_digits: bool) -> int:
    """
    Extract first and last digits in a string
    giving the concatenation of both
    """
    number_map = {word: str(index + 1) for index, word in enumerate(number_list)}
    pattern = (
        r"\d"
        if only_digits
        else r"(?=(0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
    )

    integers = re.findall(pattern, input_line)
    first, last = integers[0], integers[-1]

    if not only_digits:
        first = number_map.get(first, first)
        last = number_map.get(last, last)

    return int(first + last)


if __name__ == "__main__":
    day1_file_path = "./../../data/day1.txt"
    first_part, second_part = number_extraction(day1_file_path)
    print(f"The answer for the first part is: {first_part}")
    print(f"The answer for the second part is {second_part}")
