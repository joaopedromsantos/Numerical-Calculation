from flask import Blueprint, request

from calculations.absolute_and_relative_errors import AbsoluteAndRelativeError
from calculations.gauss_solver import GaussSolver
from API.views import success_response, error_response, information_response
from API.validators import is_valid_matrix, validate_xy_payload

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


@routes.route('/informations', methods=['GET'])
def informations():
    return information_response()

