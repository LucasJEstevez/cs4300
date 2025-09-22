import pytest
import math
from src.task3 import task3_check_sign,task3_ten_primes#,task3_product

def test_task3_check_sign():
    assert task3_check_sign(10) == 'positive'
    assert task3_check_sign(.001) == 'positive'
    assert task3_check_sign(0) == 'zero'
    assert task3_check_sign(-10) == 'negative'
    assert task3_check_sign(-.001) == 'negative'

def test_task3_primes(capfd):
    task3_ten_primes()
    out,err = capfd.readouterr()
    assert out=="[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n"

#def test_task3_product():
#    assert task3_product(100) == math.factorial(100)