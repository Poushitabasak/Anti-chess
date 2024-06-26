
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        """
        Initialize the board with an 8x8 grid and set up the initial positions of pieces.
        """
        self.grid = [[None for _ in range(8)] for _ in range(8)]  # Create an 8x8 grid initialized with None
        self.setup_board()  # Set up the initial positions of the pieces

    def setup_board(self):
        """
        Set up the initial positions of the pieces on the board.
        """
        # Place pawns
        for i in range(8):
            self.grid[1][i] = Pawn('W')  # Place white pawns on the second row
            self.grid[6][i] = Pawn('B')  # Place black pawns on the seventh row

        # Place rooks
        self.grid[0][0] = self.grid[0][7] = Rook('W')
        self.grid[7][0] = self.grid[7][7] = Rook('B')

        # Place knights
        self.grid[0][1] = self.grid[0][6] = Knight('W')
        self.grid[7][1] = self.grid[7][6] = Knight('B')

        # Place bishops
        self.grid[0][2] = self.grid[0][5] = Bishop('W')
        self.grid[7][2] = self.grid[7][5] = Bishop('B')

        # Place queens
        self.grid[0][3] = Queen('W')
        self.grid[7][3] = Queen('B')

        # Place kings
        self.grid[0][4] = King('W')
        self.grid[7][4] = King('B')

    def display(self):
        """
        Display the current state of the board in the CLI.
        """
        print("  A B C D E F G H")  # Column labels
        print(" +----------------")
        for i, row in enumerate(self.grid):
            print(f"{8 - i}|", end=" ")  # Row labels
            for cell in row:
                if cell:
                    print(cell, end=" ")  # Display piece
                else:
                    print(".", end=" ")  # Display empty square
            print(f"|{8 - i}")  # Row labels
        print(" +----------------")
        print("  A B C D E F G H")  # Column labels


    def move_piece(self, start, end):
        """
        Move a piece from the start position to the end position.
        
        :param start: Tuple (start_row, start_col)
        :param end: Tuple (end_row, end_col)
        """
        start_row, start_col = start  # Unpack start position
        end_row, end_col = end  # Unpack end position
        piece = self.grid[start_row][start_col]  # Get the piece at the start position

        if piece and piece.is_valid_move(self.grid, start, end):
            self.grid[end_row][end_col] = piece  # Move the piece to the end position
            self.grid[start_row][start_col] = None  # Empty the start position
        else:
            print("Invalid move")

    def is_valid_position(self, pos):
        """
        Check if the position is within the bounds of the board.
        
        :param pos: Tuple (row, col)
        :return: Boolean indicating if the position is valid
        """
        row, col = pos
        return 0 <= row < 8 and 0 <= col < 8