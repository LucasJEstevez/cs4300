from src.task1 import task_1_return,task_1_print
import pytest

#for a basic return stmt
def test_task_1_return():
    assert task_1_return() == "Hello world!"

#capture stdout for a print stmt
def test_task_1_print(capfd):
    task_1_print()
    out,err = capfd.readouterr()
    assert out=="Hello world!\n"

