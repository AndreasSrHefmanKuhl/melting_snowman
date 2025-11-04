from game_logic import play_game

if __name__ == '__main__':

    while True:
        play_game()

    # Ask user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing Snowman Meltdown! Goodbye.")
            break