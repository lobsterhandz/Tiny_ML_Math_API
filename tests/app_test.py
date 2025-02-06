import unittest
import json
from app import app, db
from models import MathOperation


class MathApiTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup a test database before running tests."""
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_math_operations.db"
        cls.client = app.test_client()

        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database after tests are completed."""
        with app.app_context():
            db.drop_all()

    def test_add_operation(self):
        """✅ Test Adding a Sum (Positive Case)"""
        response = self.client.post(
            "/sum",
            data=json.dumps({"operand1": 5, "operand2": 3}),
            content_type="application/json",
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertIn("result", data)
        self.assertEqual(data["result"], 8)

    def test_get_sums_by_result_valid(self):
        """✅ Test Retrieving Sums by a Valid Result"""
        response = self.client.get("/sum/result/8")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("operations", data)
        self.assertIsInstance(data["operations"], list)

    def test_get_sums_by_result_invalid(self):
        """❌ Negative Test: Retrieving Sums by a Non-Existent Result"""
        response = self.client.get("/sum/result/999999")  # A result unlikely to exist
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["message"], "No operations found with this result")

    def test_invalid_sum_request(self):
        """❌ Negative Test: Sending Invalid Data for Sum"""
        response = self.client.post(
            "/sum",
            data=json.dumps({"operand1": 10}),  # Missing operand2
            content_type="application/json",
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Both operands must be provided")


if __name__ == "__main__":
    unittest.main()
