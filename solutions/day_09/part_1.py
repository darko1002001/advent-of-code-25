import logging
from itertools import combinations

from solutions.types import Coordinate, Section
from solutions.utils import read_numbers

logger = logging.getLogger(__name__)


def calculate_area(a: Coordinate, b: Coordinate) -> int:
    x1, y1 = a
    x2, y2 = b
    return (abs(x1 - x2) + 1) * (abs(y2 - y1) + 1)


def solve(inputs: Section) -> int:
    coordinates: list[Coordinate] = [read_coordinate(input_) for input_ in inputs]
    return max([calculate_area(a, b) for a, b in combinations(coordinates, 2)])


def read_coordinate(item: str) -> Coordinate:
    i, j = read_numbers(item)
    return j, i
