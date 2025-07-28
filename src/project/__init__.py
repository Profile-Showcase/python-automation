import random

# Per your request, '0' for soldier (pawn) and 'z' for horse (knight).
PIECES = {
    "soldier": "0",
    "horse": "z",
    "rook": "r",
    "bishop": "b",
    "queen": "q",
    "king": "k",
}
EMPTY_SQUARE = "."

# To make empty squares more common, we create a weighted list of pieces.
# This gives roughly a 70% chance of a square being empty.
WEIGHTED_PIECES = (
    [EMPTY_SQUARE] * 70
    + [PIECES["soldier"]] * 5
    + [PIECES["horse"]] * 5
    + [PIECES["rook"]] * 5
    + [PIECES["bishop"]] * 5
    + [PIECES["queen"]] * 5
    + [PIECES["king"]] * 5
)


def generate_random_board(rows=8, cols=8):
    """
    Generates a board with randomly placed chess pieces.

    Returns:
        list[list[str]]: A 2D list representing the chess board.
    """
    board = []
    for _ in range(rows):
        row = [random.choice(WEIGHTED_PIECES) for _ in range(cols)]
        board.append(row)
    return board


def print_board(board):
    """
    Prints a chess board matrix to the console in a readable format.

    Args:
        board (list[list[str]]): The 2D list representing the board.
    """
    if not board:
        print("The board is empty.")
        return

    print("\n--- Random Chess Board ---")
    # Add column headers for a classic chess look.
    col_headers = "  " + " ".join([chr(ord("a") + i) for i in range(len(board[0]))])
    separator = " +" + "-" * (len(col_headers) - 1) + "+"

    print(col_headers)
    print(separator)

    # Print each row with its number.
    for i, row in enumerate(board, 1):
        print(f"{i}| {' '.join(row)} |{i}")

    print(separator)
    print(col_headers)
    print("--------------------------\n")


def main():
    """Main function to generate and print a board."""
    random_board = generate_random_board()
    print_board(random_board)


# This allows the script to be run directly.
if __name__ == "__main__":
    main()
