import pytest
import math
from src.task3 import task3_check_sign,is_prime,task3_ten_primes,task3_sum_classic,task3_sum_magic

#Testing with regular and very small numbers
def test_task3_check_sign():
    assert task3_check_sign(10) == 'positive'
    assert task3_check_sign(.001) == 'positive'
    assert task3_check_sign(0) == 'zero'
    assert task3_check_sign(-10) == 'negative'
    assert task3_check_sign(-.001) == 'negative'

#Checking output, not much to check as funciton takes no inputs
def test_task3_primes(capfd):
    task3_ten_primes()
    out,err = capfd.readouterr()
    assert out=="[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n"

#Checks for different types of sum functions
def test_task3_sum():
    assert task3_sum_classic(100) == 5050
    assert task3_sum_magic(100) == 5050

    #Edge Cases
    assert task3_sum_classic(1) == 1
    assert task3_sum_magic(1) == 1
    assert task3_sum_classic(0) == 0
    assert task3_sum_classic(0) == 0

#Tests is_prime function (will convert to integer)
def test_task3_is_prime():
    assert is_prime(1)==False
    assert is_prime(2)==True
    assert is_prime(13159)==True
    assert is_prime(50.1)==False