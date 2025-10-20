import pytest
from nanograz import example


@pytest.fixture
def input():
    return [1, 2, 3]


@pytest.fixture
def output():
    return [1, 4, 9]


def test_square(input, output):
    for i, o in zip(input, output):
        assert example.square(i) == o
