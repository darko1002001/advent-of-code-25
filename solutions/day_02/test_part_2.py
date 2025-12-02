from solutions.types import LoadTextCallable

from .part_2 import is_match, solve


def test_part_2_sample(load_text: LoadTextCallable):
    lines = load_text("input_test")
    assert solve(lines) == 4174379265


def test_part_2(load_text: LoadTextCallable):
    lines = load_text("input")
    assert solve(lines) == 19058204438


def test_match():
    assert is_match("1010") == True
