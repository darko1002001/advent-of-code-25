import logging

from solutions.types import Section

logger = logging.getLogger(__name__)


def solve(inputs: Section) -> int:
    input_ = inputs[0]
    items = input_.split(",")
    all_invalid: list[int] = []
    for item in items:
        s, e = item.split("-")
        invalid_ids = process_single(s, e)
        all_invalid.extend(invalid_ids)
    return sum(all_invalid)


def process_single(range_start: str, range_end: str) -> list[int]:
    ids: list[int] = []
    for i in range(int(range_start), int(range_end) + 1):
        if is_match(str(i)):
            ids.append(i)

    logger.info(f"{range_start=}-{range_end=} found {ids=}")
    return ids


def is_match(num: str) -> bool:
    for sl in range(1, len(num) // 2 + 1):
        sub = num[0:sl]
        repeated = sub * (len(num) // sl)
        if repeated == num:
            return True
    return False
