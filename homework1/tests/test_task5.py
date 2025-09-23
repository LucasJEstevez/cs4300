import pytest
from src.task5 import task5_getID,task5_books

#Checks books output
def test_task5_books():
    assert task5_books() == [['The Hunger Games', 'Suzanne Collins'], ['Charlie and the Chocolate Factory', 'Roald Dahl'], ["Summer of '49", 'David Halberstam']]

#Tests for task5_getID
def test_task5_getID():
    assert task5_getID('Lucas Estevez') == 42
    assert task5_getID('Daniel Barbotko') == 69
    with pytest.raises(KeyError):
        task5_getID('Mason Sowanick')==30