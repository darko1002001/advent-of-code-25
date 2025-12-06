from solutions.types import LoadSectionsCallable

from .part_1 import solve


def test_part_1_sample(load_sections: LoadSectionsCallable):
    lines = load_sections("input_test")
    assert solve(lines) == 3


def test_part_1(load_sections: LoadSectionsCallable):
    lines = load_sections("input")
    assert solve(lines) == -1
