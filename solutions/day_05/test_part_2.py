from solutions.types import LoadSectionsCallable

from .part_2 import solve


def test_part_2_sample(load_sections: LoadSectionsCallable):
    lines = load_sections("input_test")
    assert solve(lines) == 14


def test_part_2(load_sections: LoadSectionsCallable):
    lines = load_sections("input")
    assert solve(lines) == -1
