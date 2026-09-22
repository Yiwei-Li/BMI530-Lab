"""A tiny number-guessing game designed for learning pytest."""

import random


def check_guess(secret: int, guess: int) -> str:
	"""Return a hint for a guess."""
	if guess < 1 or guess > 10:
		raise ValueError("guess must be between 1 and 20")
	if guess < secret:
		return "too low"
	if guess > secret:
		return "too high"
	return "correct"


def play_game(secret: int | None = None) -> None:
	"""Play until the user guesses the secret number."""
	secret = secret if secret is not None else random.randint(1, 20)
	print("I am thinking of a number from 1 to 20.")

	while True:
		try:
			guess = int(input("Your guess: "))
			result = check_guess(secret, guess)
		except ValueError as error:
			print(f"Invalid guess: {error}")
			continue

		print(result)
		if result == "correct":
			print("You win!")
			return


if __name__ == "__main__":
	play_game()
