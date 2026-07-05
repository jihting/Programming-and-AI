"""Week 3 Lab 4 starter: Tic-Tac-Toe engine.

Copy this file into your own week-3 folder and rename it to tictactoe.py.
Complete the TODO sections during the lab.
"""


WINNING_LINES = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


class Board:
    def __init__(self):
        self.cells = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def __str__(self):
        rows = []
        for row in self.cells:
            rows.append(" | ".join(row))
        return "\n---------\n".join(rows)

    def legal_moves(self):
        """Return a list of empty (row, column) positions."""
        # TODO: build and return the list of legal moves.
        return []

    def make_move(self, row, column, player):
        """Place player at row, column if the move is legal."""
        # TODO: reject out-of-bounds moves.
        # TODO: reject moves into occupied cells.
        # TODO: update the board and return True.
        return False

    def check_winner(self):
        """Return 'X', 'O', or None."""
        # TODO: check every line in WINNING_LINES.
        return None

    def is_draw(self):
        """Return True if the board is full and nobody has won."""
        # TODO: check winner first, then legal moves.
        return False


if __name__ == "__main__":
    board = Board()
    print(board)
    print("Legal moves:", board.legal_moves())
