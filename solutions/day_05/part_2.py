import logging

from solutions.types import Section

logger = logging.getLogger(__name__)

type Range = tuple[int, int]
type Ranges = list[Range]


def solve(inputs: list[Section]) -> int:
    ranges = load_ranges(inputs[0])
    ranges = merge_ranges(ranges)
    count = 0
    for l, r in ranges:
        diff = r - l + 1
        logger.info(f"{l:_}-{r:_} - {diff}")
        count += diff
    return count


def merge_ranges(ranges: Ranges) -> Ranges:
    new_ranges: Ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        last = new_ranges.pop()
        current = ranges[i]

        if current[0] <= last[1]:
            last = last[0], max(last[1], current[1])
            new_ranges.append(last)
        else:
            new_ranges.append(last)
            new_ranges.append(current)

    return new_ranges


def load_ranges(section: Section) -> Ranges:
    ranges: Ranges = []
    for range in section:
        l, r = range.split("-")
        ranges.append((int(l), int(r)))
    ranges.sort()
    return ranges
