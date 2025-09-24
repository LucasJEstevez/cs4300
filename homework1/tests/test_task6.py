import pytest
from src.task6 import task6_read_file

#Tests task6 (I found the 104 by putting the text through an online word counter)
def test_task6_read_file():
    assert task6_read_file() == 104