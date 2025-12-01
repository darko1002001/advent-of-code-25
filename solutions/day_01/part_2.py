import logging

from solutions.types import Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    current = 50
    count = 0
    for input_ in inputs:
        direction = input_[0]
        rotations = int(input_[1:])
        over = rotations // 100
        count += over
        rotations = rotations % 100
        if direction == "R":
            turn = rotations + current
            if turn >= 100:
                count += 1
            next_ = turn % 100
        else:
            next_ = current - rotations
            if next_ <= 0 and current > 0:
                count += 1
            if next_ < 0:
                next_ = 100 + next_
        current = next_
    return count
