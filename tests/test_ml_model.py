import unittest
from ml.ml_model import TinyMLMath

class TestTinyMLMath(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize the TinyML model once for all tests"""
        cls.ml_model = TinyMLMath()

    def test_addition(self):
        """✅ Test Addition"""
        self.assertEqual(self.ml_model.predict_math(5, 3, 0), 8)

    def test_subtraction(self):
        """✅ Test Subtraction"""
        self.assertEqual(self.ml_model.predict_math(10, 4, 1), 6)

    def test_multiplication(self):
        """✅ Test Multiplication"""
        self.assertEqual(self.ml_model.predict_math(6, 5, 2), 30)

    def test_division(self):
        """✅ Test Division"""
        self.assertEqual(self.ml_model.predict_math(20, 4, 3), 5)

    def test_division_by_zero(self):
        """❌ Test Division by Zero (should return an error message)"""
        self.assertEqual(self.ml_model.predict_math(10, 0, 3), "Undefined (Division by zero)")

    def test_invalid_operation(self):
        """❌ Test Invalid Operation (should return an error)"""
        with self.assertRaises(ValueError):
            self.ml_model.predict_math(5, 2, 999)  # Invalid operation index

if __name__ == "__main__":
    unittest.main()
