# test_transformations.py
import unittest
from transformations import MultiplyByTwo

class TestMultiplyByTwo(unittest.TestCase):
    def test_map(self):
        # Instantiate the MultiplyByTwo function.
        func = MultiplyByTwo()
        # Test a few cases.
        self.assertEqual(func.map(3), 6)
        self.assertEqual(func.map(0), 0)
        self.assertEqual(func.map(-2), -4)

if __name__ == '__main__':
    unittest.main()
