"""Week 3 Lab 4 optional game-loop template.

Use this if your tutor asks you to keep the game loop separate from the Board class.
"""

from tictactoe import Board


def ask_for_move():
    """Ask the current player for a row and column.

    TODO: improve this so it handles non-numeric input without crashing.
    """
    row = int(input("Row (0, 1, 2): "))
    column = int(input("Column (0, 1, 2): "))
    return row, column


def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"


def main():
    board = Board()
    current_player = "X"

    while True:
        print(board)
        print("Current player:", current_player)

        row, column = ask_for_move()

        if not board.make_move(row, column, current_player):
            print("That move is not allowed. Try again.")
            continue

        winner = board.check_winner()
        if winner is not None:
            print(board)
            print(winner, "wins")
            break

        if board.is_draw():
            print(board)
            print("Draw")
            break

        current_player = switch_player(current_player)


if __name__ == "__main__":
    main()
