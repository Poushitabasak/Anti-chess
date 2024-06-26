from board import Board

class Game:
    def __init__(self):
        """
        Initialize the game with a board and set the current player to white.
        """
        self.board = Board()  # Create a new board instance
        self.current_player = 'W'  # Set the starting player to white
        self.game_over = False  # Initialize game over flag to False

    def switch_player(self):
        """
        Switch the current player from white to black or vice versa.
        """
        self.current_player = 'B' if self.current_player == 'W' else 'W'  # Switch current player

    def parse_position(self, pos):
        """
        Parse a board position string (e.g., 'A2') into a tuple of indices (row, col).
        
        :param pos: Board position as a string
        :return: Tuple (row, col)
        """
        col = ord(pos[0].upper()) - ord('A')  # Convert column letter to index
        row = 8 - int(pos[1])  # Convert row number to index
        return row, col  # Return parsed position as tuple

    def play(self):
        """
        Start the game loop where players alternate turns to make moves.
        """
        while not self.game_over:
            self.board.display()  # Display the current state of the board
            print(f"Player {self.current_player}'s turn")

            move = input("Enter your move (e.g., A2 B4) or 'display' to show the board, 'quit' to exit: ").strip()
            if move.lower() == 'quit':
                print(f"Player {self.current_player} quits. Player {self.current_player} loses.")
                self.game_over = True
                continue

            if move.lower() == 'display':
                self.board.display()
                continue

            try:
                start_pos, end_pos = move.split()
                start = self.parse_position(start_pos)
                end = self.parse_position(end_pos)

                # Validate positions
                if not self.board.is_valid_position(start) or not self.board.is_valid_position(end):
                    print("Invalid position. Try again.")
                    continue

                # Get the piece at the start position
                piece = self.board.grid[start[0]][start[1]]

                if piece is None:
                    print("No piece at the start position. Try again.")
                    continue

                if piece.color != self.current_player:
                    print("It's not your piece. Try again.")
                    continue

                # Move the piece
                if piece.is_valid_move(self.board.grid, start, end):
                    self.board.move_piece(start, end)
                    self.switch_player()
                else:
                    print("Invalid move. Try again.")

            except ValueError:
                print("Invalid input format. Please enter the move in the format 'A2 B4'.")
            except Exception as e:
                print(f"An error occurred: {e}. Try again.")
