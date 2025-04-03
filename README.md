# Numerical Calculation API

## Overview
The **Gauss API** is a Flask-based web service that solves linear systems using the Gaussian elimination method. Clients can send a matrix via a JSON request, and the API returns the computed solutions.

## Features
- Solve linear systems using Gaussian elimination.
- Handle errors gracefully with proper response messages.
- Provide an informational endpoint for API details.

## Installation

### Prerequisites
- Python 3.x
- Flask
- Numpy
- Gunicorn

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd Numerical_Calculation_API
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the API
Start the Flask server with:
```sh
flask run
```

By default, the API will be available at `http://127.0.0.1:5000`.

### Endpoints

#### Solve a Linear System
- **URL:** `/API/gauss`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "matrix": [[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]]
  }
  ```
- **Response:**
  ```json
  {
    "solutions": [3.0, -2.5, 7.0]
  }
  ```

#### API Information
- **URL:** `/API/informations`
- **Method:** `GET`
- **Response:** API details and usage instructions.

## Error Handling
The API returns JSON-formatted error messages in case of invalid input, such as:
```json
{
  "error": "Invalid format. Send a JSON with the key 'matrix'."
}
```

## License
This project is open-source. Feel free to contribute or modify it as needed.

## Contact
For questions or contributions, open an issue on the repository or contact the developer.

