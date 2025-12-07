import logging

from solutions.types import Coordinate, Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    start = find_start(inputs[0])
    return drop(inputs, start)


def find_start(row: str) -> Coordinate:
    for j, ch in enumerate(row):
        if ch == "S":
            return 0, j
    raise ValueError("No start found")


def drop(inputs: Section, start: Coordinate) -> int:
    current: list[Coordinate] = [start]
    count = 0
    seen: set[Coordinate] = set()
    while len(current):
        i, j = current.pop(0)
        di = i + 1
        dj = j
        if di >= len(inputs):
            continue

        ch = inputs[di][dj]
        if (di, dj) in seen:
            continue
        seen.add((di, dj))
        if ch == ".":
            current.append((di, dj))
        elif ch == "^":
            count += 1
            current.append((di, dj - 1))
            current.append((di, dj + 1))
    return count
