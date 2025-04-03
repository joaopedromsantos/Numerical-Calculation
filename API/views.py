from flask import jsonify

def success_response(solutions):
    """ Returns a JSON response with the solutions. """
    return jsonify({"solutions": solutions})

def error_response(message, code=400):
    """ Returns a JSON error response. """
    return jsonify({"error": message}), code

def information_response():
    """ Returns a JSON response with system information. """
    return jsonify(
        {
            "API Name": "Numerical Calculation API",
            "Version": "1.0.0",
            "Status": "Running",
            "Endpoints": {
                "/API/gauss": "Solves a system of linear equations using Gaussian Elimination",
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
        }, 200
    )
