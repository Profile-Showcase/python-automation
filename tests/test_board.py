from unittest.mock import patch

import pytest

from project import (
    generate_random_board,
    print_board,
    main,
    PIECES,
    EMPTY_SQUARE
)


# 1. Test Board Dimensions
def test_generate_board_dimensions():
    """Verify the board is generated with the default 8x8 dimensions."""
    board = generate_random_board()
    assert len(board) == 8, "Board should have 8 rows"
    for row in board:
        assert len(row) == 8, "Each row should have 8 columns"


# 2. Test for Valid Piece Characters
def test_generate_board_has_valid_pieces():
    """Ensure every cell on the board contains a valid piece character."""
    board = generate_random_board()
    valid_chars = set(PIECES.values()) | {EMPTY_SQUARE}
    for row in board:
        for piece in row:
            assert piece in valid_chars, f"Invalid piece '{piece}' found on board"


# 3. Test Printing a Non-Empty Board
def test_print_board_with_non_empty_board(capsys):
    """Check that print_board executes without error for a standard board."""
    board = generate_random_board()
    print_board(board)
    captured = capsys.readouterr()
    assert "--- Random Chess Board ---" in captured.out
    assert " +----------------+" in captured.out


# 4. Test Printing an Empty Board
def test_print_board_with_empty_board(capsys):
    """Verify print_board handles an empty list gracefully."""
    print_board([])
    captured = capsys.readouterr()
    assert "The board is empty." in captured.out


# 5. Test Main Function Execution
@patch('project.generate_random_board')
@patch('project.print_board')
def test_main_function_does_not_error(mock_print, mock_generate):
    """Confirm the main function can be called without raising an exception."""
    mock_board = [['.']]
    mock_generate.return_value = mock_board
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an unexpected exception: {e}")

    mock_generate.assert_called_once()
    mock_print.assert_called_once_with(mock_board)


# 6. Test Board Randomness
def test_board_is_random():
    """Generate two boards and assert they are not identical."""
    board1 = generate_random_board()
    board2 = generate_random_board()
    # While there's a tiny chance of collision, it's astronomically low
    # for an 8x8 board and serves as a good-enough check for randomness.
    assert board1 != board2, "Two generated boards should not be identical"
