# game_logic.py
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum allowed mistakes is one less than the number of stages
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Prints the current snowman stage, the masked word, and game stats."""

    # Clearer Display Enhancement
    print("-" * 40)
    print(f"| Mistakes: {mistakes} / {MAX_MISTAKES} | Remaining: {MAX_MISTAKES - mistakes} |")
    print("-" * 40)

    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    is_word_guessed = True
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            is_word_guessed = False

    print("Word: ", display_word)
    print("Guessed letters: ", ", ".join(sorted(guessed_letters)))
    print("\n")

    return is_word_guessed


def get_valid_guess(guessed_letters):
    """Prompts the user for a guess with Input Validation."""
    while True:
        guess = input("Guess a letter: ").lower()

        # Input Validation Enhancement
        if not guess.isalpha():
            print("🚨 Invalid guess. Please enter an alphabetical character only.")
            continue

        if len(guess) != 1:
            print("🚨 Invalid guess. Please enter *only one* letter at a time.")
            continue

        if guess in guessed_letters:
            print(f"🚨 You already guessed '{guess}'. Try a different letter.")
            continue

        return guess


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    game_over = False

    print("Welcome to Snowman Meltdown!")
    print(f"The secret word has {len(secret_word)} letters.")

    # --- Main Game Loop ---
    while not game_over:
        is_word_guessed = display_game_state(mistakes, secret_word, guessed_letters)

        # Check for immediate win
        if is_word_guessed:
            print(f"*** 🏆 CONGRATULATIONS! You saved the snowman! 🏆 ***")
            print(f"The word was '{secret_word}'.")
            game_over = True
            continue

        # Check for loss
        if mistakes >= MAX_MISTAKES:
            print(STAGES[MAX_MISTAKES])
            print("--- 🥶 GAME OVER! The snowman melted! 🥵 ---")
            print(f"The word was '{secret_word}'.")
            game_over = True
            continue

        # Get and process valid guess
        guess = get_valid_guess(guessed_letters)

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"** ✅ Correct! The letter '{guess}' is in the word. **")
        else:
            print(f"-- ❌ Incorrect! The letter '{guess}' is not in the word. --")
            mistakes += 1





