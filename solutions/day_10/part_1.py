import logging
import re
from itertools import combinations

from solutions.types import Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    return sum([min_clicks(input_) for input_ in inputs])


def min_clicks(row: str) -> int:
    signal = find_signal(row)
    buttons: list[list[int]] = find_buttons(row)
    for i in range(len(buttons) + 1):
        for c in combinations(buttons, i):
            if is_valid(c, signal):
                return i
    return 0


def is_valid(buttons: list[list[int]], expected: str) -> bool:
    start = ["."] * len(expected)
    for b in buttons:
        for pos in b:
            if start[pos] == ".":
                start[pos] = "#"
            else:
                start[pos] = "."

    return "".join(start) == expected


def find_signal(row: str):
    pattern = re.compile(r"\[(.*?)\]")
    iter_ = pattern.finditer(row)
    return list(i.group(1) for i in iter_)[0]


def find_buttons(row: str):
    pattern = re.compile(r"\((.*?)\)")
    iter_ = pattern.finditer(row)
    return list(list(map(int, i.group(1).split(","))) for i in iter_)
