"""Test for my functions."""

from main_function import *
from encouragement_color import *
from fortune_color import *
from task_color import *

def test_start():

    assert callable(start)

def test_encouragement_color():
    
    assert callable(red_button_chosen)
    assert callable(green_button_chosen)
    assert callable(blue_button_chosen)
    assert callable(purple_button_chosen)

def test_fortune_color():
    
    assert callable(red_button_chosen)
    assert callable(green_button_chosen)
    assert callable(blue_button_chosen)
    assert callable(purple_button_chosen)
    
def test_task_color():
    
    assert callable(red_button_chosen)
    assert callable(green_button_chosen)
    assert callable(blue_button_chosen)
    assert callable(purple_button_chosen)