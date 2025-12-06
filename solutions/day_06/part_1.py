import logging
from math import prod

from solutions.types import Section
from solutions.utils import read_non_whitespace, read_numbers

logger = logging.getLogger(__name__)

operations = {"+": sum, "*": prod}


def solve(inputs: Section) -> int:
    nums = [read_numbers(in_) for in_ in inputs][:-1]
    operators = read_non_whitespace(inputs[-1])
    n_columns = len(nums[0])
    n = len(nums)

    sum = 0
    for j in range(n_columns):
        operator = operators[j]
        values = [nums[i][j] for i in range(n)]
        sum += operations[operator](values)

    return sum
