import pytest
from Lab02.series import fibonacci, lucas, sum_series

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5

def test_lucas():
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11

def test_sum_series():
    assert sum_series(5) == fibonacci(5)  # Default values should give fibonacci series
    assert sum_series(5, 2, 1) == lucas(5)  # 2 and 1 as optional parameters should give lucas series

    # Test another series with custom values for a and b
    a, b = 3, 4
    assert sum_series(0, a, b) == a
    assert sum_series(1, a, b) == b
    assert sum_series(2, a, b) == a + b
    assert sum_series(3, a, b) == a + 2 * b
