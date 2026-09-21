import pytest

from app import check_guess


@pytest.mark.parametrize(
	("guess", "expected"),
	[(2, "too low"), (8, "too high"), (5, "correct")],
)
def test_check_guess(guess: int, expected: str) -> None:
	assert check_guess(secret=5, guess=guess) == expected


def test_guess_must_be_between_one_and_ten() -> None:
	with pytest.raises(ValueError, match="between 1 and 10"):
		check_guess(secret=5, guess=11)
