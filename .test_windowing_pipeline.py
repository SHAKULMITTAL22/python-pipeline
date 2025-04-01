import unittest
from windowing_pipeline import run_pipeline

class TestWindowingPipeline(unittest.TestCase):

    def test_windowing_logic(self):
        # Mocked data for testing
        result = run_pipeline()
        expected_result = [('Alice', 8), ('Bob', 9)]

        self.assertEqual(sorted(result), sorted(expected_result))

if __name__ == '__main__':
    unittest.main()
