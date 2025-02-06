from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MathOperation(db.Model):
    """Model to store mathematical operations and their results."""
    id = db.Column(db.Integer, primary_key=True)
    operand1 = db.Column(db.Float, nullable=False)
    operand2 = db.Column(db.Float, nullable=False)
    operation = db.Column(db.String(10), nullable=False)  # e.g., "addition", "subtraction"
    result = db.Column(db.Float, nullable=False)

    def __init__(self, operand1, operand2, operation, result):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation
        self.result = result

    def to_dict(self):
        """Convert model instance to a dictionary format."""
        return {
            "id": self.id,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "operation": self.operation,
            "result": self.result
        }
