import pytest

from app import check_guess


def test_correct_guess():
    assert check_guess(5, 5) == "correct"


def test_guess_too_low():
    assert check_guess(5, 3) == "too low"


def test_guess_too_high():
    assert check_guess(5, 8) == "too high"


@pytest.mark.parametrize("guess", [0, 21])
def test_invalid_guess(guess):
    with pytest.raises(ValueError):
        check_guess(5, guess)