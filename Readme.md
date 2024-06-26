# Anti-Chess CLI Game

This project is a simple implementation of Anti-Chess (also known as Losing Chess) for two players to play on the command line interface (CLI). The rules are the same as standard chess, but the goal is to sacrifice all your pieces before your opponent does.

## How to Run the Code

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. Ensure Python is Installed

3. Run the Game 
python chess.py

How to Play the Game:
1. Starting the Game
When you run the game, the initial board setup will be displayed, and it will be player W's (White's) turn to move.

2. Input Your Move

Moves should be entered in the form A2 B3, where A2 is the starting square and B3 is the ending square.
To display the current state of the board, type display.
To quit the game, type quit.

3. Game Rules

The goal is to lose all your pieces.
If a player can capture a piece, they must do so.
If there are multiple captures available, the player can choose which piece to capture.
Players alternate turns, with White going first.

4. Example Moves

For White (W) to move a pawn from A2 to A3, input: A2 A3.
For Black (B) to move a pawn from A7 to A6, input: A7 A6.

5. Switching Turns
After a valid move, the game will automatically switch turns to the other player.

6. Invalid Moves
If you enter an invalid move, the game will prompt you to try again.

**Example Game Play**
  A B C D E F G H
 +----------------
8| r n b q k b n r |8
7| p p p p p p p p |7
6| . . . . . . . . |6
5| . . . . . . . . |5
4| . . . . . . . . |4
3| . . . . . . . . |3
2| P P P P P P P P |2
1| R N B Q K B N R |1
 +----------------
  A B C D E F G H
Player W's turn
Enter your move (e.g., A2 B4) or 'display' to show the board, 'quit' to exit: A2 A3

  A B C D E F G H
 +----------------
8| r n b q k b n r |8
7| p p p p p p p p |7
6| . . . . . . . . |6
5| . . . . . . . . |5
4| . . . . . . . . |4
3| P . . . . . . . |3
2| . P P P P P P P |2
1| R N B Q K B N R |1
 +----------------
  A B C D E F G H
Player B's turn
Enter your move (e.g., A7 A6) or 'display' to show the board, 'quit' to exit: A7 A6
