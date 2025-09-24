from src.task1 import task1_return,task1_print
import pytest

#for a basic return stmt
def test_task1_return():
    assert task1_return() == "Hello world!"

#capture stdout for a print stmt
def test_task1_print(capfd):
    task1_print()
    out,err = capfd.readouterr()
    assert out=="Hello world!\n"

