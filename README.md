
# 🔢 Numerical Calculation API

## 🧠 Overview
The **Numerical Calculation API** is a Flask-based web service designed to perform numerical computations like solving systems of linear equations using **Gaussian Elimination** and calculating **absolute and relative errors**. The API is easy to use and built with Python, Flask, and NumPy.

## 🚀 Public API

Access the public version of this API at:  
🔗 **https://numerical-calculation.onrender.com**

---

## ⚙️ Installation

### Prerequisites

- Python 3.x  
- Flask  
- NumPy  
- Gunicorn *(optional for deployment)*

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Numerical_Calculation_API
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Start the Flask server locally:

```bash
flask run
```

By default, the API will be available at:  
📍 `http://127.0.0.1:5000`

---

## 📡 Endpoints

### 📍 `POST /API/gauss`

Solves a system of linear equations using Gaussian Elimination.

#### ➤ Request:
```json
{
  "matrix": [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
  ]
}
```

#### ✅ Response:
```json
{
  "success": true,
  "data": {
    "a1": [3, "3"],
    "a2": [-2.5, "-5/2"],
    "a3": [7, "7"]
  }
}

```

---

### 📍 `POST /API/absolute_and_relative_errors`

Calculates absolute and relative errors between `x` and `y`.

#### ➤ Request:
```json
{
  "x": 5.2,
  "y": 5.3
}
```

#### ✅ Response:
```json
{
  "success": true,
  "data": {
    "absolute": [0.1, "1/10"],
    "relative": [0.0188679245, "1/53"],
    "relative_percentage": 1.8867924528,
    "top_quota_absolute_error": [0.5, "1/2"],
    "x": 5.2,
    "y": 5.3
  }
}
```

---

### 📍 `GET /API/informations`

Returns general information about the API, including developer details.

---

## ❌ Error Handling

If an invalid input is provided, the API will return a clear JSON error message.

#### Example:
```json
{
  "success": false,
  "error": "..."
}
```

---

## 📄 License

This project is open-source and licensed under the **MIT License**.  
Feel free to use, modify, and contribute!

---

## 📬 Contact

For questions or contributions, please open an issue on the repository or contact:

**João Pedro Martins dos Santos**  
📧 joaopedrosantos.dev@gmail.com  
🔗 [GitHub](https://github.com/joaopedromsantos)  
🔗 [LinkedIn](https://www.linkedin.com/in/joaopedrosantosdev/)
