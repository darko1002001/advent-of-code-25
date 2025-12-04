import logging

from solutions.types import Coordinate, Grid, Section
from solutions.utils import (
    OMNI_DIRECTIONS,
    to_modifiable_grid,
    traverse_grid,
    within_grid_bounds,
)

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    grid = to_modifiable_grid(inputs)
    total = 0
    while True:
        items = find_items_to_remove(grid)
        if len(items) == 0:
            break
        total += len(items)
        for i, j in items:
            grid[i][j] = "."
    return total


def find_items_to_remove(grid: Grid) -> list[Coordinate]:
    items: list[Coordinate] = []
    for i, j, ch in traverse_grid(grid):
        if ch != "@":
            continue
        if check(grid, i, j):
            items.append((i, j))
    return items


def check(grid: Grid, i: int, j: int) -> int:
    occupied_slots = 0
    for di, dj in OMNI_DIRECTIONS:
        ni = i + di
        nj = j + dj
        if within_grid_bounds(grid, ni, nj):
            if grid[ni][nj] == "@":
                occupied_slots += 1
    return 1 if occupied_slots < 4 else 0
