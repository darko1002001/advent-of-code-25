import logging

from solutions.types import Grid, Section
from solutions.utils import OMNI_DIRECTIONS, traverse_grid, within_grid_bounds

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    return sum(
        [ch == "@" and check(inputs, i, j) for i, j, ch in traverse_grid(inputs)]
    )


def check(grid: Grid, i: int, j: int) -> int:
    occupied_slots = 0
    for di, dj in OMNI_DIRECTIONS:
        ni = i + di
        nj = j + dj
        if within_grid_bounds(grid, ni, nj):
            if grid[ni][nj] == "@":
                occupied_slots += 1
    return 1 if occupied_slots < 4 else 0
