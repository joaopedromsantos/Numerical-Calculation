from fractions import Fraction


def convert_to_decimal_and_fraction(variable_names: list, values, decimal_places: int = 10,
                                    max_denominator: int = 100000):
    """
    Converts a list of values into a dictionary with rounded decimals and fractions.

    :param variable_names: List of variable names (e.g. ['x', 'y']).
    :param values: List of float values corresponding to the variable names.
    :param decimal_places: Number of decimal places to round to (default = 10).
    :param max_denominator: Maximum denominator for the fraction (default = 1000).
    :return: Dictionary like {'x': [0.1111111111, '1/9'], ...}
    """
    result = {}
    for name, value in zip(variable_names, values):
        frac = Fraction(value).limit_denominator(max_denominator)
        result[name] = [round(float(value), decimal_places), str(frac)]
    return result
