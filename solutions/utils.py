import re

from solutions.types import Grid, ModifiableGrid

DIRECTIONS_MAP = {"R": (0, 1), "U": (-1, 0), "D": (1, 0), "L": (0, -1)}
DIRECTIONS_ARROWS_MAP = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
OMNI_DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def to_modifiable_grid(grid: Grid) -> ModifiableGrid:
    return [list(row) for row in grid]


def traverse_grid(grid: Grid):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            yield i, j, value


def read_numbers(value: str) -> list[int]:
    pattern = re.compile(r"(-?\d+)")
    iter_ = pattern.finditer(value)
    return list(map(int, [i.group(1) for i in iter_]))


def within_grid_bounds(grid: Grid, i: int, j: int) -> bool:
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    return True
