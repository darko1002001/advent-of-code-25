from solutions.types import LoadTextCallable

from .part_2 import solve


def test_part_2_sample(load_text: LoadTextCallable):
    lines = load_text("input_test2")
    assert solve(lines) == 2


def test_part_2(load_text: LoadTextCallable):
    lines = load_text("input")
    assert solve(lines) == 370500293582760
