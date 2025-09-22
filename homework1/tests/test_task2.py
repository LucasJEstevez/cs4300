import pytest
from src.task2 import exponent, concat, mod

def test_task2_exponent():
    assert exponent(2,3)==8
    assert exponent(2,-1)==.5

def test_task2_concat():
    assert concat(6,9)=='69'
    assert concat('f',0)=='f0'

def test_task1_mod():
    assert mod(5,2)==1
    assert mod(6,9) == 6
