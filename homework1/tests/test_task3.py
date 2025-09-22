import pytest
from src.task3 import check_sign

def test_task3_positive_large():
    assert check_sign(10) == 'positive'

def test_task3_positive_small():
    assert check_sign(.001) == 'positive'

def test_task3_positive_zero():
    assert check_sign(0) == 'zero'

def test_task3_negative_large():
    assert check_sign(-10) == 'negative'

def test_task3_negative_small():
    assert check_sign(-.001) == 'negative'