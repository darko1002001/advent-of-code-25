import logging

from solutions.types import Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    return sum([find_max(input_) for input_ in inputs])


def find_max(row: str) -> int:
    n = len(row)
    current_index = 0
    result = ""
    for battery_index in range(11, -1, -1):
        max = current_index
        for i in range(current_index, n - battery_index):
            if row[i] > row[max]:
                max = i
        current_index = max + 1
        result += row[max]

    logger.info(f"result for {row=} is {result=}")
    return int(result)
