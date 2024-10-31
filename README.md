# Versus-AI-Tic-Tac-Toe
This Game implementing AI to play against users

## Overview

This project involves building an AI agent to play Tic-Tac-Toe optimally using the `Minimax` algorithm. The AI aims to make the best possible move at each stage, either maximizing or minimizing the outcome based on the current player's perspective.

## AI Logic and Strategy

The AI uses the `Minimax` algorithm to evaluate each possible game state, ensuring it plays optimally. The functions in this project support the game's rules, logic, and decision-making process for the AI.

## Implementation Tasks

Complete the following methods in `tictactoe.py`:

### Core Functions

1. **`player(board)`**: Determines the current player (`X` or `O`) for the given board state.
   - In the initial state, `X` moves first. After each move, players alternate turns.
   - Any output is acceptable if a terminal (completed) board is given.

2. **`actions(board)`**: Returns a set of all possible moves for the given board.
   - Each move is represented as a tuple `(i, j)` where `i` is the row (0, 1, or 2) and `j` is the column (0, 1, or 2).
   - Possible moves are limited to empty cells.
   - For terminal boards, any return value is acceptable.

3. **`result(board, action)`**: Returns a new board state based on the specified action without modifying the original board.
   - Raises an exception if the action is invalid.
   - Creates a deep copy of the board with the action applied to avoid altering the original.

4. **`winner(board)`**: Determines the winner, if any, on the current board.
   - Returns `X` if `X` has won, `O` if `O` has won, or `None` if there is no winner.
   - A win is defined by three identical marks in a row, column, or diagonal.

5. **`terminal(board)`**: Checks if the game is over.
   - Returns `True` if a player has won or all cells are filled without a winner.
   - Returns `False` if the game is still ongoing.

6. **`utility(board)`**: Calculates the utility value of a terminal board.
   - Returns `1` if `X` has won, `-1` if `O` has won, and `0` for a tie.
   - Assumes the board is terminal when called.

7. **`minimax(board)`**: Determines the optimal move for the player on the given board.
   - Returns the optimal action `(i, j)` among allowable moves.
   - If multiple moves are equally optimal, any may be chosen.
   - For terminal boards, returns `None`.


## Usage:

Requires Python(3) and Python package installer pip(3) to run:

Install requirements:
$pip3 install -r requirements.txt

Run Game:
$python3 runner.py

## Demo Video:
Check out a [demo video](https://drive.google.com/file/d/14lhgdW1Nfqcc3N3MKdeFUBcXElHv09i9/view?usp=sharing) to see the Tic-Tac-Toe AI in action!



## Further Ideas:

* Applying Alpha-Beta Pruning for better efficiency.
