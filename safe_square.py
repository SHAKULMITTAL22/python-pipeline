import pytest
from pyflink.datastream.functions import MapFunction

# Custom MapFunction that squares the input value but raises an exception for negatives.
class SafeSquare(MapFunction):
    def map(self, value):
        if value < 0:
            raise ValueError("Negative values not allowed")
        return value * value

# Test successful cases with multiple inputs using parameterization.
@pytest.mark.parametrize("input_value, expected", [
    (2, 4),
    (3, 9),
    (0, 0),
    (-1, "Negative values not allowed"),
])
def test_safe_square_success(input_value, expected):
    func = SafeSquare()
    result = func.map(input_value)
    assert result == expected

# Test that a negative input raises a ValueError.
def test_safe_square_exception():
    func = SafeSquare()
    with pytest.raises(ValueError):
        func.map(-1)
