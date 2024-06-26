#Script working as the main to run the game
from game import Game

def main():
    """
    Main function to start the chess game.
    """
    game = Game()  # Create a new game instance
    game.play()    # Start the game loop

if __name__ == "__main__":
    main()  # Run the main function if the script is executed
