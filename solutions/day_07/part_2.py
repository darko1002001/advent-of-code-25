import logging

from solutions.types import Coordinate, Section

logger = logging.getLogger(__name__)


type Memo = dict[Coordinate, int]


def solve(inputs: Section) -> int:
    start = find_start(inputs[0])
    return drop(inputs, {}, start)


def find_start(row: str) -> Coordinate:
    for j, ch in enumerate(row):
        if ch == "S":
            return 0, j
    raise ValueError("No start found")


def drop(inputs: Section, memo: Memo, current: Coordinate) -> int:
    i, j = current
    if i >= len(inputs):
        return 1

    if current in memo:
        return memo[current]
    ch = inputs[i][j]
    val = 0
    if ch == "." or ch == "S":
        val = drop(inputs, memo, (i + 1, j))
    elif ch == "^":
        val = drop(inputs, memo, (i + 1, j - 1)) + drop(inputs, memo, (i + 1, j + 1))
    memo[current] = val
    return val
