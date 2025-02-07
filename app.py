from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException
import os

from database.models import db, MathOperation
from ml.ml_model import TinyMLMath  # Import TinyMLMath model
from config import CurrentConfig
# Initialize Flask App
app = Flask(__name__)
app.config.from_object(CurrentConfig)
tiny_ml = TinyMLMath()  # Load the ML model

# Initialize Database and Migrations
db.init_app(app)
migrate = Migrate(app, db)

CORS(app)  # Enable CORS for all routes

# **💡 ROUTES - API ENDPOINTS** #

@app.route("/")
def home():
    """Root Endpoint - API Status Check"""
    return jsonify({"message": "Math API is running!", "status": "success"}), 200


@app.route("/sum", methods=["POST"])
def add_operation():
    """
    📌 **Add a Sum**
    Request: JSON { "operand1": float, "operand2": float }
    Response: JSON { "id": int, "operand1": float, "operand2": float, "operation": "addition", "result": float }
    """
    try:
        data = request.get_json()
        operand1 = data.get("operand1")
        operand2 = data.get("operand2")

        # Validation: Ensure numbers are provided
        if operand1 is None or operand2 is None:
            return jsonify({"error": "Both operands must be provided"}), 400

        # Perform Addition
        result = operand1 + operand2

        # Store Operation in Database
        operation = MathOperation(operand1=operand1, operand2=operand2, operation="addition", result=result)
        db.session.add(operation)
        db.session.commit()

        return jsonify(operation.to_dict()), 201

    except Exception as e:
        return handle_exception(e)


@app.route("/sum/result/<int:target_result>", methods=["GET"])
def get_sums_by_result(target_result):
    """
    📌 **Retrieve Sums Filtered by Result**
    Request: GET `/sum/result/<int:target_result>`
    Response: JSON { "operations": [...] }
    """
    try:
        operations = MathOperation.query.filter_by(result=target_result).all()
        if not operations:
            return jsonify({"message": "No operations found with this result"}), 404

        return jsonify({"operations": [op.to_dict() for op in operations]}), 200

    except Exception as e:
        return handle_exception(e)


@app.route("/sum/all", methods=["GET"])
def get_all_sums():
    """
    📌 **Retrieve All Sums**
    Request: GET `/sum/all`
    Response: JSON { "operations": [...] }
    """
    try:
        operations = MathOperation.query.all()
        return jsonify({"operations": [op.to_dict() for op in operations]}), 200

    except Exception as e:
        return handle_exception(e)

@app.route("/predict_math", methods=["GET"])
def predict_math():
    """Handles math prediction requests."""
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        operation = int(request.args.get("operation"))  # 0=Add, 1=Subtract, 2=Multiply, 3=Divide
        
        if operation not in [0, 1, 2, 3]:
            return jsonify({"error": "Invalid operation. Use 0 for add, 1 for subtract, 2 for multiply, 3 for divide."}), 400
        
        result = tiny_ml.predict_math(a, b, operation)
        return jsonify({"a": a, "b": b, "operation": operation, "result": result})
    
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input. Ensure a and b are numbers and operation is 0-3."}), 400


# **💡 ERROR HANDLING - GLOBAL EXCEPTION HANDLER** #

@app.errorhandler(Exception)
def handle_exception(e):
    """Global Exception Handler for All Errors"""
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error", "details": str(e)}), 500


# **💡 DEPLOYMENT - RUN APP** #

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables exist before running
    print("✅ Flask API running on Render...")
    app.run(host="0.0.0.0", port=5000, debug=True)
