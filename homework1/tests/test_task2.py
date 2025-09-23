import pytest
from src.task2 import task2_exponent_integers, task2_exponent_floats, task2_concat, task2_mod

#Tests integer exponent function
def task2_exponent_integers():
    assert task2_exponent(2,3)==8
    assert task2_exponent(2,-1)==.5
    assert task2_exponent(9,.5) == 1

#Tests float exponent function
def task2_exponent_floats():
    assert task2_exponent(2,3)==8
    assert task2_exponent(2,-1)==.5
    assert task2_exponent(9,.5) == 3

#Tests concatenate function
def test_task2_concat():
    assert task2_concat(6,9)=='69'
    assert task2_concat('f',0)=='f0'
    assert task2_concat(.5,4)=='0.54'

#Tests mod function
def test_task1_mod():
    assert task2_mod(5,2)==1
    assert task2_mod(6,9) == 6
    assert task2_mod(2,.3) == .2

    #Checks if division by 0 raises error
    with pytest.raises(ZeroDivisionError):
        task2_mod(4,0)
        task2_mod(6,0)
