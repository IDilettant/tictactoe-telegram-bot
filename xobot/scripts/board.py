"""Board module."""
from xobot.scripts.player import PLAYER_O, PLAYER_X

DIMENSION = 3
marker_to_char = {
    None: ' . ',
    PLAYER_X: ' x ',
    PLAYER_O: ' o ',
}


def show_board(current_state):
    """Print current state of board.

    Args:
        current_state (list): board current state
    """
    for row in range(DIMENSION):
        line = []
        for col in range(DIMENSION):
            line.append(marker_to_char[current_state[row][col]])
        print(''.join(line))


def has_row_win(current_state):
    """Check for a win horizontally.

    Args:
        current_state (list): board current state

    Returns:
        bool
    """
    for row in range(DIMENSION):
        unique_rows = set(current_state[row])
        if len(unique_rows) == 1:
            if unique_rows.pop() is not None:
                return True
    return False


def has_col_win(current_state):
    """Check for a win vertically.

    Args:
        current_state (list): board current state

    Returns:
        bool
    """
    for col in range(DIMENSION):
        unique_cols = set()
        for row in range(DIMENSION):
            unique_cols.add(current_state[row][col])
        if len(unique_cols) == 1:
            if unique_cols.pop() is not None:
                return True
    return False


def has_diagonal_win(current_state):
    """Check for a win diagonally.

    Args:
        current_state (list): board current state

    Returns:
        bool
    """
    # check backwards diagonal (top left to bottom right)
    backwards_diag = set()
    backwards_diag.add(current_state[0][0])
    backwards_diag.add(current_state[1][1])
    backwards_diag.add(current_state[2][2])
    if len(backwards_diag) == 1:
        if backwards_diag.pop() is not None:
            return True
    # check forwards diagonal (bottom left to top right)
    forwards_diag = set()
    forwards_diag.add(current_state[2][0])
    forwards_diag.add(current_state[1][1])
    forwards_diag.add(current_state[0][2])
    if len(forwards_diag) == 1:
        if forwards_diag.pop() is not None:
            return True
    return False


def has_win(current_state):
    """Check for the win.

    Args:
        current_state (list): board current state

    Returns:
        bool
    """
    return has_row_win(
        current_state,
    ) or has_col_win(
        current_state,
    ) or has_diagonal_win(
        current_state,
    )


def get_legal_moves(current_state):
    """Get coordinates of possible moves.

    Args:
        current_state (list): board current state

    Returns:
        Coordinates of possible moves
    """
    possible_choices = []
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            # Check the board position is empty
            if current_state[row][col] is None:
                possible_choices.append([row, col])
    return possible_choices


def make_move(current_state, row, col, player):
    """Change board current state based on the move made.

    Args:
        current_state (list): board current state
        row (int): board row index
        col (int): board col index
        player (int): current player

    Returns:
        Board current state
    """
    if current_state[row][col] in get_legal_moves(current_state):
        current_state[row][col] = player
    return current_state