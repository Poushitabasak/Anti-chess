class Piece:
    def __init__(self, color):
        """
        Initialize a piece with a given color.
        
        :param color: 'W' for white or 'B' for black
        """
        self.color = color  # Set the piece color

    def __str__(self):
        """
        Return the string representation of the piece.
        
        :return: String representation
        """
        return f"{self.color}{self.symbol}"  # Return piece color and symbol

    def is_valid_move(self, board, start_pos, end_pos):
        """
        Check if a move is valid for this piece. Must be overridden by subclasses.
        
        :param board: Current board state
        :param start_pos: Starting position tuple (row, col)
        :param end_pos: Ending position tuple (row, col)
        :return: Boolean indicating if the move is valid
        """
        raise NotImplementedError("This method should be overridden by subclasses")  # Placeholder for subclass implementation

class Pawn(Piece):
    symbol = 'P'

    def is_valid_move(self, board, start_pos, end_pos):
        """
        Validate the move for a pawn based on simplified movement rules.
        
        :param board: Current board state
        :param start_pos: Starting position tuple (row, col)
        :param end_pos: Ending position tuple (row, col)
        :return: Boolean indicating if the move is valid
        """
        direction = 1 if self.color == 'W' else -1  # Determine move direction based on color
        start_row, start_col = start_pos  # Unpack start position
        end_row, end_col = end_pos  # Unpack end position

        # Check if the move is a valid forward move
        if start_col == end_col:
            if (end_row - start_row) == direction:
                return True  # Allow one step forward
            elif (self.color == 'W' and start_row == 1 and end_row == 3) or (self.color == 'B' and start_row == 6 and end_row == 4):
                return True  # Allow two steps forward from the starting position

        return False  # If none of the conditions are met, the move is invalid

class Rook(Piece):
    symbol = 'R'

    def is_valid_move(self, board, start_pos, end_pos):
        """
        Validate the move for a rook.
        
        :param board: Current board state
        :param start_pos: Starting position tuple (row, col)
        :param end_pos: Ending position tuple (row, col)
        :return: Boolean indicating if the move is valid
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # Rook moves in straight lines
        if start_row == end_row or start_col == end_col:
            step_row = (end_row - start_row) // max(1, abs(end_row - start_row))
            step_col = (end_col - start_col) // max(1, abs(end_col - start_col))
            for i in range(1, max(abs(end_row - start_row), abs(end_col - start_col))):
                if board[start_row + i * step_row][start_col + i * step_col] is not None:
                    return False  # There's a piece in the way
            return True
        return False

class Knight(Piece):
    symbol = 'N'

    def is_valid_move(self, board, start_pos, end_pos):
        """
        Validate the move for a knight.
        
        :param board: Current board state
        :param start_pos: Starting position tuple (row, col)
        :param end_pos: Ending position tuple (row, col)
        :return: Boolean indicating if the move is valid
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # Knight moves in L shapes
        if (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]:
            return True
        return False

class Bishop(Piece):
    symbol = 'B'

    def is_valid_move(self, board, start_pos, end_pos):
        """
        Validate the move for a bishop.
        
        :param board: Current board state
        :param start_pos: Starting position tuple (row, col)
        :param end_pos: Ending position tuple (row, col)
        :return: Boolean indicating if the move is valid
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # Bishop moves diagonally
        if abs(start_row - end_row) == abs(start_col - end_col):
            step_row = (end_row - start_row) // abs(end_row - start_row)
            step_col = (end_col - start_col) // abs(end_col - start_col)
            for i in range(1, abs(end_row - start_row)):
                if board[start_row + i * step_row][start_col + i * step_col] is not None:
                    return False  # There's a piece in the way
            return True
        return False

class Queen(Piece):
    symbol = 'Q'

    def is_valid_move(self, board, start_pos, end_pos):
        """
        Validate the move for a queen.
        
        :param board: Current board state
        :param start_pos: Starting position tuple (row, col)
        :param end_pos: Ending position tuple (row, col)
        :return: Boolean indicating if the move is valid
        """
        # Queen combines the moves of rook and bishop
        return Rook(self.color).is_valid_move(board, start_pos, end_pos) or Bishop(self.color).is_valid_move(board, start_pos, end_pos)

class King(Piece):
    symbol = 'K'

    def is_valid_move(self, board, start_pos, end_pos):
        """
        Validate the move for a king.
        
        :param board: Current board state
        :param start_pos: Starting position tuple (row, col)
        :param end_pos: Ending position tuple (row, col)
        :return: Boolean indicating if the move is valid
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        # King moves one square in any direction
        if max(abs(start_row - end_row), abs(start_col - end_col)) == 1:
            return True
        return False
