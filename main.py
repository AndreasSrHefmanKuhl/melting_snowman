# main.py
from game_logic import play_game

if __name__ == "__main__":
    # Initialize the score dictionary
    game_score = {'wins': 0, 'losses': 0}

    print("Welcome to Snowman Meltdown!")

    while True:
        # Pass the score dictionary to play_game
        play_game(game_score)

        # Ask user if they want to play again
        print(f"\n--- Current Score: Wins: {game_score['wins']}, Losses: {game_score['losses']} ---")
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            print("\nThanks for playing Snowman Meltdown!")
            print(f"Final Score: Wins: {game_score['wins']}, Losses: {game_score['losses']}")
            break