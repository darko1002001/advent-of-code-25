import logging

from solutions.types import Section
from solutions.utils import read_numbers

logger = logging.getLogger(__name__)

type PackageQuantitiesDict = dict[int, int]
type Package = list[str]
type PackagesDict = dict[int, Package]
type GridShape = list[int]


def solve(inputs: list[Section]) -> int:
    package_quantities: PackageQuantitiesDict = {}
    for i in range(6):
        section = inputs[i]
        package = section[1:]
        package_quantities[i] = sum(
            [1 if ch == "#" else 0 for p in package for ch in p]
        )
    grids = inputs[-1]
    return sum([calculate_grid(grid, package_quantities) for grid in grids])


def calculate_grid(grid: str, package_quantities: PackageQuantitiesDict) -> int:
    l, r = grid.split(": ")
    shape = read_numbers(l)
    quantities = read_numbers(r)
    if same_square(shape, quantities) or same_count(
        shape, quantities, package_quantities
    ):
        return 1

    logger.info(f"{grid} might require further investigation")
    return 0


def same_count(
    shape: GridShape, quantities: list[int], package_quantities: PackageQuantitiesDict
) -> bool:
    """
    Calculate the total points from each package based on quantities, assume you can fit them somehow in the required shape.
    If the shape can fit all points then return true
    """
    w, h = shape
    shape_count = w * h
    package_count = sum(package_quantities[i] * val for i, val in enumerate(quantities))
    return shape_count >= package_count


def same_square(shape: GridShape, quantities: list[int]) -> bool:
    """
    You need to fit 'quantities' amount of 3x3 squares in the shape. Return true if you can
    """
    w, h = shape
    shape_count = w * h
    package_count = sum(q * 3 * 3 for q in quantities)

    return shape_count >= package_count
