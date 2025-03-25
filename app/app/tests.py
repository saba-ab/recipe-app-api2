from django.test import SimpleTestCase
from app.calc import add, subtract, divide

class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add(self):
        """Testing adding numbers"""
        res = add(1, 2)
        self.assertEqual(res, 3)

    def test_subtract(self):
        """Testing subtracting numbers"""

        res = subtract(10, 4)

        self.assertEqual(res, 6)

    def test_divide(self):
        """Testing dividing numbers"""

        res = divide(10, 2)

        self.assertEqual(res, 5)

