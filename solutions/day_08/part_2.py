import logging
from itertools import combinations
from typing import cast

from solutions.types import Section
from solutions.union_find import UnionFind
from solutions.utils import read_numbers

logger = logging.getLogger(__name__)

type Coordinate3 = tuple[int, int, int]
type DistancesDict = dict[tuple[Coordinate3, Coordinate3], int]
type SortedDistancesList = list[tuple[tuple[Coordinate3, Coordinate3], int]]


def get_first_three(row_: str) -> Coordinate3:
    data = read_numbers(row_)
    if len(data) < 3:
        raise ValueError("List must have at least 3 elements")

    return cast(Coordinate3, tuple(data[:3]))


def calculate_distance(a: Coordinate3, b: Coordinate3) -> int:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2)


def solve(inputs: Section) -> int:
    rows: list[Coordinate3] = [get_first_three(row_) for row_ in inputs]
    distances: DistancesDict = {
        (a, b): calculate_distance(a, b) for a, b in combinations(rows, 2)
    }
    sorted_distances = list(sorted(distances.items(), key=lambda item: item[1]))

    n = len(rows)
    l = 0
    r = len(sorted_distances)
    result: int = 0
    while l < r:
        mid = l + (r - l) // 2
        val = connect(sorted_distances, n, mid)
        if val is None:
            l = mid + 1
        else:
            result = val
            r = mid
    return result


def connect(sorted_distances: SortedDistancesList, n: int, amount: int) -> int | None:
    djs = UnionFind[Coordinate3]()
    for i in range(amount):
        a, _ = sorted_distances[i]
        x, y = a
        _ = djs.union(x, y)

    component, *_ = djs.get_largest_components(1)
    if len(component) == n:
        a, _ = sorted_distances[amount - 1]
        x, y = a
        return x[0] * y[0]
    return None
