import logging
from itertools import combinations
from math import prod
from typing import cast

from solutions.types import Section
from solutions.union_find import UnionFind
from solutions.utils import read_numbers

logger = logging.getLogger(__name__)

type Coordinate3 = tuple[int, int, int]
type DistancesDict = dict[tuple[Coordinate3, Coordinate3], int]


def get_first_three(row_: str) -> Coordinate3:
    data = read_numbers(row_)
    if len(data) < 3:
        raise ValueError("List must have at least 3 elements")

    return cast(Coordinate3, tuple(data[:3]))


def calculate_distance(a: Coordinate3, b: Coordinate3) -> int:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2)


def solve(inputs: Section, amount: int) -> int:
    rows: list[Coordinate3] = [get_first_three(row_) for row_ in inputs]
    distances: DistancesDict = {
        (a, b): calculate_distance(a, b) for a, b in combinations(rows, 2)
    }
    return connect(distances, amount)


def connect(distances: DistancesDict, amount: int) -> int:
    sorted_distances = list(sorted(distances.items(), key=lambda item: item[1]))
    djs = UnionFind[Coordinate3]()
    for i in range(amount):
        a, _ = sorted_distances[i]
        x, y = a
        _ = djs.union(x, y)

    components = djs.get_largest_components(3)
    return prod([len(component) for component in components])
