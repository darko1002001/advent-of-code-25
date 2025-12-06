import logging
import typing
from math import prod

from solutions.types import Section
from solutions.utils import read_numbers

logger = logging.getLogger(__name__)

type NumbersArrayOperator = typing.Callable[[list[int]], int] | None


def solve(inputs: Section) -> int:
    operation_values: list[int] = []
    operator: NumbersArrayOperator = None
    total = 0
    n_columns = len(inputs[0])
    for col in reversed(range(n_columns)):
        str_column = read_column(inputs, col)
        if op := read_operator(str_column):
            operator = op
        numbers = read_numbers(str_column)
        if len(numbers) > 0:
            operation_values.append(numbers[0])
        else:
            total += calculate(operation_values, operator)
            operation_values = []
            operator = None
    total += calculate(operation_values, operator)
    return total


def read_operator(value: str) -> NumbersArrayOperator:
    if "+" in value:
        return sum
    if "*" in value:
        return prod
    return None


def calculate(values: list[int], operator: NumbersArrayOperator) -> int:
    if operator is None:
        raise ValueError("operator must be defined")
    return operator(values)


def read_column(inputs: Section, col_number: int) -> str:
    return "".join([row[col_number] for row in inputs])
