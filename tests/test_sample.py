import pytest
from main import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

#def test_failure_example():
#    assert subtract(5, 2) == 1  # Intentional failure for demonstration
