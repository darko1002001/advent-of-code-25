import logging

from solutions.types import Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    return sum([find_max(input_) for input_ in inputs])


def find_max(row: str) -> int:
    n = len(row)
    a_index = 0
    for i in range(0, n - 1):
        if row[i] > row[a_index]:
            a_index = i

    b_index = a_index + 1
    for i in range(b_index, n):
        if row[i] > row[b_index]:
            b_index = i
    return int(row[a_index] + row[b_index])
