from flask import Blueprint, request
from calculations.gauss_solver import GaussSolver
from API.views import success_response, error_response, information_response

routes = Blueprint('routes', __name__, url_prefix='/API')


@routes.route('/gauss', methods=['POST'])
def solve_gauss():
    """ Route that receives a matrix and returns the solution of the system. """
    data = request.get_json()

    if not data or "matrix" not in data:
        return error_response("Invalid format. Send a JSON with the key 'matrix'.")

    matrix = data["matrix"]
    if not isinstance(matrix, list):
        return error_response("The matrix must be a list of lists.")

    try:
        solver = GaussSolver(matrix)
        solutions = solver.solve()
        return success_response(solutions)
    except Exception as e:
        return error_response(str(e), 500)


@routes.route('/informations', methods=['GET'])
def informations():
    return information_response()

