from solutions.types import LoadSectionsCallable

from .part_1 import solve


def test_part_1_sample(load_sections: LoadSectionsCallable):
    sections = load_sections("input_test")
    assert solve(sections) == 2


def test_part_1(load_sections: LoadSectionsCallable):
    sections = load_sections("input")
    assert solve(sections) == 546
