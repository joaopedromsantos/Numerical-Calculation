from flask import jsonify


def success_response(data):
    """ Returns a JSON response with the solutions. """
    return jsonify({"success": True, "data": data}), 200


def error_response(message, code=400):
    """ Returns a JSON error response. """
    return jsonify({"success": False, "error": message}), code


def information_response():
    """ Returns a JSON response with system information. """
    return jsonify(
        {
                "success": True,
                "data": {
                    "API Name": "Numerical Calculation API",
                    "Version": "1.0.0",
                    "Status": "Running",
                    "Endpoints": {
                        "/API/gauss": "Solves a system of linear equations using Gaussian Elimination",
                        "/API/absolute_and_relative_errors": "Calculates absolute and relative errors from two "
                                                             "numeric values.",
                        "/API/info": "Returns API information"
                    },
                    "Developer": {
                        "Name": "João Pedro Martins dos Santos",
                        "Email": "joaopedrosantos.dev@gmail.com",
                        "GitHub": "https://github.com/joaopedromsantos",
                        "LinkedIn": "https://www.linkedin.com/in/joaopedrosantosdev/"
                    },
                    "Technologies": ["Python", "Flask", "NumPy"],
                    "License": "MIT"
                }
        }
    ), 200
