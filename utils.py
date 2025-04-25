from fractions import Fraction


def convert_to_decimal_and_fraction(variable_names: list, values, decimal_places: int = 10,
                                    max_denominator: int = 100000):
    """
    Converts a list of values into a dictionary with rounded decimals and fractions.
    Also generates the polynomial equation as a string.

    :param variable_names: List of variable names (e.g. ['a1', 'a2', 'a3']).
    :param values: List of float values corresponding to the variable names.
    :param decimal_places: Number of decimal places to round to (default = 10).
    :param max_denominator: Maximum denominator for the fraction (default = 100000).
    :return: Dictionary like {'a1': [decimal, 'fraction'], ..., 'equation': 'P(x) = ...'}
    """
    result = {}
    for name, value in zip(variable_names, values):
        frac = Fraction(value).limit_denominator(max_denominator)
        result[name] = [round(float(value), decimal_places), str(frac)]

    coefficients = [result[f'a{i+1}'][1] for i in range(len(variable_names))]
    result['equation'] = format_polynomial_equation(coefficients)

    return result


def format_polynomial_equation(coefficients):
    """
    Formats a polynomial equation string like: P(x) = a + b*x + c*x^2

    :param coefficients: List of string fractions like ['13/2', '-501/140', '87/140']
    :return: Equation string
    """
    termos = []

    for i, frac in enumerate(coefficients):
        if frac in ['0']:
            continue
        if i == 0:
            termos.append(f"{frac}")
        elif i == 1:
            termos.append(f"{frac}*x")
        else:
            termos.append(f"{frac}*x^{i}")

    equation = "P(x) = " + " + ".join(termos)
    return equation.replace("+ -", "- ")
