from flask import Blueprint, request

from calculations.absolute_and_relative_errors import AbsoluteAndRelativeError
from calculations.gauss_solver import GaussSolver
from API.views import success_response, error_response, information_response
from API.validators import is_valid_matrix, validate_xy_payload
from calculations.polynomialfitsolver import PolynomialFitSolver

routes = Blueprint('routes', __name__, url_prefix='/API')


@routes.route('/gauss', methods=['POST'])
def solve_gauss():
    """ Route that receives a matrix and returns the solution of the system. """
    data = request.get_json()

    if not data or "matrix" not in data:
        return error_response("Invalid format. Send a JSON with the key 'matrix'.")

    matrix = data["matrix"]

    if not is_valid_matrix(matrix):
        return error_response("The matrix must be a list of lists containing only numbers.")

    try:
        solver = GaussSolver(matrix)
        solutions = solver.solve()
        return success_response(solutions)
    except Exception as e:
        return error_response(str(e), 500)


@routes.route('/absolute_and_relative_errors', methods=['POST'])
def solve_absolute_and_relative_errors():
    """ Route that calculates absolute and relative errors. """
    data = request.get_json()

    is_valid, result = validate_xy_payload(data)

    if not is_valid:
        return error_response(result)

    x, y = result

    try:
        solver = AbsoluteAndRelativeError(x, y)
        solutions = solver.solve()
        return success_response(solutions)
    except Exception as e:
        return error_response(str(e), 500)


@routes.route('/polynomial-fit', methods=['POST'])
def polynomial_fit():
    """ Route that receives x and y data and returns the polynomial fit coefficients. """
    data = request.get_json()

    if not data or "x" not in data or "y" not in data:
        return error_response("Invalid format. Send a JSON with keys 'x' and 'y'.")

    x = data["x"]
    y = data["y"]

    if not isinstance(x, list) or not isinstance(y, list):
        return error_response("Both 'x' and 'y' must be lists of numbers.")

    try:
        solver = PolynomialFitSolver(x, y)
        solutions = solver.solve()
        return success_response(solutions)
    except Exception as e:
        return error_response(str(e), 500)


@routes.route('/informations', methods=['GET'])
def informations():
    return information_response()

