# test_pipeline.py
import unittest
from pipeline import run_pipeline

class TestPipeline(unittest.TestCase):
    def test_pipeline_output(self):
        # Define input data.
        input_data = [1, 2, 3, 4]
        # The expected output is each element multiplied by 2.
        expected_output = [2, 4, 6, 8]
        # Run the pipeline.
        output = run_pipeline(input_data)
        # Assert the output matches the expected output.
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
