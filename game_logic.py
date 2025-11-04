# game_logic.py
import random
from ascii_art import STAGES  # Import the STAGES art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum allowed mistakes is one less than the number of stages
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Prints the current snowman stage and the masked word."""
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
            is_word_guessed = False  # If any letter is missing, the word isn't guessed

    print("Word: ", display_word)
    print("Guessed letters: ", ", ".join(sorted(guessed_letters)))
    print(f"Mistakes remaining: {MAX_MISTAKES - mistakes}")
    print("\n")

    return is_word_guessed


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    game_over = False

    print("Welcome to Snowman Meltdown!")
    print(f"The secret word has {len(secret_word)} letters.")

    # --- Main Game Loop ---
    while not game_over:
        # 1. Display current state and check for win
        is_word_guessed = display_game_state(mistakes, secret_word, guessed_letters)

        # Check for immediate win (if all letters were guessed in the last turn)
        if is_word_guessed:
            print(f"*** CONGRATULATIONS! You saved the snowman! ***")
            print(f"The word was '{secret_word}'.")
            game_over = True
            continue  # Skip to the end of the loop

        # Check for loss
        if mistakes >= MAX_MISTAKES:
            print(STAGES[MAX_MISTAKES])  # Display fully melted snowman
            print("--- GAME OVER! ---")
            print(f"The snowman melted. The word was '{secret_word}'.")
            game_over = True
            continue  # Skip to the end of the loop

        # 2. Get and validate guess
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        # 3. Process guess
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"** Correct! The letter '{guess}' is in the word. **")
        else:
            print(f"-- Incorrect! The letter '{guess}' is not in the word. --")
            mistakes += 1  # Increment mistakes


if __name__ == "__main__":
    play_game()