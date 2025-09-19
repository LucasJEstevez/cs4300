from src.task1 import f,g
import pytest

#for a basic return stmt
def test_task_1():
    assert f() == "Hello world!"

#capture stdout for a print stmt
def test_task_2(capfd):
    g()
    out,err = capfd.readouterr()
    assert out=="Hello world!\n"

