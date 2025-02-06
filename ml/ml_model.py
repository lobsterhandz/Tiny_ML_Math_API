import os

class TinyMLMath:
    def __init__(self):
        """Simple rule-based model for math operations (0 = add, 1 = subtract, 2 = multiply, 3 = divide)."""
        self.operations = {
            0: lambda a, b: a + b,  # Addition
            1: lambda a, b: a - b,  # Subtraction
            2: lambda a, b: a * b,  # Multiplication
            3: lambda a, b: a / b if b != 0 else "Undefined (Division by zero)",  # Division
        }

    def predict_math(self, a, b, operation):
        """Predicts the result based on operation index."""
        if operation not in self.operations:
            raise ValueError("Invalid operation. Use 0 for add, 1 for subtract, 2 for multiply, 3 for divide.")
        
        return self.operations[operation](a, b)  # Return the calculated result


# Instantiate model
tiny_ml = TinyMLMath()

if __name__ == "__main__":
    print(f"🔢 Addition: 7 + 3 = {tiny_ml.predict_math(7, 3, 0)}")
    print(f"➖ Subtraction: 10 - 4 = {tiny_ml.predict_math(10, 4, 1)}")
    print(f"✖ Multiplication: 6 * 5 = {tiny_ml.predict_math(6, 5, 2)}")
    print(f"➗ Division: 20 / 4 = {tiny_ml.predict_math(20, 4, 3)}")
