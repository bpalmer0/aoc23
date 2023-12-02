from typing import List

# sevenine -> se7en9ne
# nineight -> n9nei8ht
# fiveight -> f5veig8t
# twone -> t2o1e
# oneight -> o1ei8ht
# eightwo -> ei8ht2o
word_to_number = {
    "one": "o1e",
    "two": "t2o",
    "three": "thr3e",
    "four": "fo4r",
    "five": "f5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "n9ne",
}

def replace_numbers(line: str) -> str:
    for word, repl in word_to_number.items():
        line = line.replace(word, repl)
    return line


def get_calibration_value(line: str) -> int:
    line = replace_numbers(line)
    digits = list(filter(lambda c: c.isdigit(), line))
    first = digits[0]
    last = digits[~0]
    return int(first + last)


def sum_calibration_values(document: List[str]):
    return sum(list(map(get_calibration_value, document)))


if __name__ == "__main__":
    with open("./input") as f:
        lines = f.readlines()
    sum = sum_calibration_values(lines)
    print(sum)
