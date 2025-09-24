import pytest
import numpy as np

#Adds arrays together, built-in feature of numpy
from src.task7 import task7_array_add
def test_task7_array_add():
    arr1 = np.array([1,2,3])
    arr2 = np.array([4,5,6])
    total_arr = np.array([5,7,9])

    assert np.array_equal(task7_array_add(arr1,arr2),total_arr)