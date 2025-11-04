import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()

    # 1. Greets the user.
    print("Welcome to Snowman Meltdown!")

    # 2. Secret word selected (displayed for testing).
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # 3. Contains an empty game loop (simulated by a single prompt for now).
    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()