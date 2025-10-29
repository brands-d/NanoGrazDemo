import pytest
from nanograz.example import custom_match


@pytest.fixture
def text():
    return "A cat, a car, and a carr were in the cartr."


def test_regex(text):
    assert custom_match(text, regex=r"car") == ["car", "car", "car"]
    assert custom_match(text, regex=r"car?") == ["ca", "car", "car", "car"]
    assert custom_match(text, regex=r"car+") == ["car", "carr", "car"]
    assert custom_match(text, regex=r"car*?") == ["ca", "ca", "ca", "ca"]
