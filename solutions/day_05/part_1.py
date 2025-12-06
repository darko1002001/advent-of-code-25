import logging

from solutions.types import Section

logger = logging.getLogger(__name__)

type Range = tuple[int, int]
type Ranges = list[Range]


def solve(inputs: list[Section]) -> int:
    ranges = load_ranges(inputs[0])
    logger.info(f"{ranges=}")
    count = 0
    for id_ in inputs[1]:
        i = int(id_)
        count += 1 if in_range(ranges, i) else 0

    return count


def in_range(ranges: Ranges, value: int) -> bool:
    for l, r in ranges:
        if value >= l and value <= r:
            return True

    return False


def load_ranges(section: Section) -> Ranges:
    ranges: Ranges = []
    for range in section:
        l, r = range.split("-")
        ranges.append((int(l), int(r)))
    ranges.sort()
    return ranges
