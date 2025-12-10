import logging
import re

from z3 import Int, Optimize, Sum, sat

from solutions.types import Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    return sum([min_clicks(input_) for input_ in inputs])


def min_clicks(row: str) -> int:
    buttons: list[list[int]] = find_buttons(row)
    jolting = find_jolting(row)

    # Not my z3 code.
    opt = Optimize()
    press_counts = [Int(f"c_{i}") for i in range(len(buttons))]

    # button press count must >= 0
    for count in press_counts:
        opt.add(count >= 0)

    # pick which button affects which joltage index
    for pos, jol in enumerate(jolting):
        affects = [press_counts[idx] for idx, btn in enumerate(buttons) if pos in btn]
        opt.add(Sum(affects) == jol)

    # minimize total presses
    opt.minimize(Sum(press_counts))

    if opt.check() == sat:
        model = opt.model()
        return sum(model[c].as_long() for c in press_counts)
    else:
        raise ValueError("No solution found")


def find_jolting(row: str):
    pattern = re.compile(r"\{(.*?)\}")
    iter_ = pattern.finditer(row)
    return list(list(map(int, i.group(1).split(","))) for i in iter_)[0]


def find_buttons(row: str):
    pattern = re.compile(r"\((.*?)\)")
    iter_ = pattern.finditer(row)
    return list(list(map(int, i.group(1).split(","))) for i in iter_)
