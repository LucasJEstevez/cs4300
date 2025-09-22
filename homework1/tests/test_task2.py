import pytest
from src.task2 import exponent, concat, mod

def test_task2_exponent():
    assert exponent(2,3)==8

def test_task2_concat_1():
    assert concat(6,9)=='69'

def test_task2_concat_2():
    assert concat('f',0)=='f0'

def test_task1_mod_1():
    assert mod(5,2)==1

def test_task_mod_2():
    assert mod(6,9) == 6
