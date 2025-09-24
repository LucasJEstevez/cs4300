import pytest
from src.task4 import calculate_discount

def test_task4_calculate_discount():
    #Test with integers
    assert calculate_discount(1,15)==.85
    assert calculate_discount(100,15)==85
    
    #Test with floats
    assert calculate_discount(9.99,10)==8.99
    assert calculate_discount(10,21.5)==7.85
    assert calculate_discount(5.50,29.5)==3.88