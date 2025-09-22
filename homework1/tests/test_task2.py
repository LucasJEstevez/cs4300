import pytest
from src.task2 import task2_exponent, task2_concat, task2_mod

def test_task2_exponent():
    assert task2_exponent(2,3)==8
    assert task2_exponent(2,-1)==.5

def test_task2_concat():
    assert task2_concat(6,9)=='69'
    assert task2_concat('f',0)=='f0'

def test_task1_mod():
    assert task2_mod(5,2)==1
    assert task2_mod(6,9) == 6
