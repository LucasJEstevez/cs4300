import pytest
from src.task5 import task5_getID,task5_books

def test_task5_books():
    assert task5_books() == [['The Hunger Games', 'Suzanne Collins'], ['Charlie and the Chocolate Factory', 'Roald Dahl'], ["Summer of '49", 'David Halberstam']]

def test_task5_getID():
    assert task5_getID('Lucas Estevez') == 42
    assert task5_getID('Daniel Barbotko') == 69