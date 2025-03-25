from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add(self):
        """Testing adding numbers"""
        res = calc.add(1, 2)
        self.assertEqual(res, 3)

    def test_subtract(self):
        """Testing subtracting numbers"""

        res = calc.subtract(10, 4)

        self.assertEqual(res, 6)