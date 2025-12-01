import logging

from solutions.types import Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    current = 50
    count = 0
    for input_ in inputs:
        direction = input_[0]
        rotations = int(input_[1:])
        rotations = rotations % 100
        if direction == "R":
            next_ = (rotations + current) % 100
        else:
            next_ = current - rotations
            if next_ < 0:
                next_ = 100 + next_
        current = next_
        if current == 0:
            count += 1
    return count
