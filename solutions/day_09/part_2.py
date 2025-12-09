import logging
from itertools import combinations

from shapely.geometry import Polygon, box

from solutions.types import Coordinate, Section
from solutions.utils import read_numbers

logger = logging.getLogger(__name__)


def calculate_area(a: Coordinate, b: Coordinate) -> int:
    x1, y1 = a
    x2, y2 = b
    return (abs(x1 - x2) + 1) * (abs(y2 - y1) + 1)


def solve(inputs: Section) -> int:
    coordinates: list[Coordinate] = [read_coordinate(input_) for input_ in inputs]
    poly = Polygon(coordinates)
    sorted_area_coordinates = sorted_squares_by_area(coordinates)
    for a, b, area in sorted_area_coordinates:
        x1, y1 = a
        x2, y2 = b
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        b = box(min_x, min_y, max_x, max_y)
        if poly.covers(b):
            return area
    return 0


def sorted_squares_by_area(
    coordinates: list[Coordinate],
) -> list[tuple[Coordinate, Coordinate, int]]:
    extended = [(a, b, calculate_area(a, b)) for a, b in combinations(coordinates, 2)]
    extended.sort(key=lambda item: item[2], reverse=True)
    return extended


def read_coordinate(item: str) -> Coordinate:
    i, j = read_numbers(item)
    return j, i
