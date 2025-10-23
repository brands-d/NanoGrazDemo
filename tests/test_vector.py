import pytest

from nanograz.OOP.vector import Vector


@pytest.fixture
def a():
    return Vector(1, 2)


@pytest.fixture
def b():
    return Vector(3, 4)


def test_vector_addition(a, b):
    c = a + b

    assert repr(c) == "2D-Vector: (4, 6)"
