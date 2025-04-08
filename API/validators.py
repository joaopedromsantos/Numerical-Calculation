def is_valid_matrix(matrix):
    """Checks if the matrix is a list of lists containing only numbers."""
    return (
        isinstance(matrix, list) and
        all(
            isinstance(row, list) and
            all(isinstance(val, (int, float)) for val in row)
            for row in matrix
        )
    )


def validate_xy_payload(data):
    """
    Validates that the dictionary contains 'x' and 'y' keys with numeric values.
    Returns a tuple (ok: bool, result: tuple or error message)
    """
    try:
        x = float(data["x"])
        y = float(data["y"])
        return True, (x, y)
    except (KeyError, ValueError, TypeError):
        return False, "Invalid format. Send a JSON with keys 'x' and 'y' (int or float)."
