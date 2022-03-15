"""Set of numbers displayed after selecting blue or purple after task."""

import ipywidgets as widgets
from ipywidgets import VBox, HBox
from IPython.display import display
import time

# Set of buttons shown after player selects blue or purple
three_button = widgets.Button(description='3')
four_button = widgets.Button(description='4')
seven_button = widgets.Button(description='7')
eight_button = widgets.Button(description='8')
out = widgets.Output()

# Arranges the buttons into a 2x2 table
left_box = VBox([three_button, seven_button])
right_box = VBox([four_button, eight_button])
out_greater = HBox([left_box, right_box])
        
display(out_greater, out)

def three_chosen(clicked):
    """After the three button is chosen, a statement corresponding 
    to the three button will be shown along with a thank you statement. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    print('Thanks for playing!') : string
        A statement thanking the player.
    """    
    with out: 
        print('\nHere is your task:\n' 
              '\nEat an apple (or any fruit of your choice)\n')
        # Delays return statement to give player time to read task
        time.sleep(1.5)
        
    return print('Thanks for playing!')

# Allows this function to occur only when the three button is clicked on 
three_button.on_click(three_chosen)

def four_chosen(clicked):
    """After the four button is chosen, a statement corresponding 
    to the four button will be shown along with a thank you statement. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    print('Thanks for playing!') : string
        A statement thanking the player.
    """  
    with out:
        print('\nHere is your task:\n' 
              '\nTreat yourself with your favorite dessert!\n')
        # Delays return statement to give player time to read task
        time.sleep(1.5)

    return print('Thanks for playing!')

# Allows this function to occur only when the four button is clicked on 
four_button.on_click(four_chosen)

def seven_chosen(clicked):
    """After the seven button is chosen, a statement corresponding 
    to the seven button will be shown along with a thank you statement. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    print('Thanks for playing!') : string
        A statement thanking the player.
    """ 
    with out:
        print('\nHere is your task:\n' 
              '\nTake a 5 minute break\n')
        # Delays return statement to give player time to read task
        time.sleep(1.5)
        
    return print('Thanks for playing!')

# Allows this function to occur only when the seven button is clicked on
seven_button.on_click(seven_chosen)   

def eight_chosen(clicked):
    """After the eight button is chosen, a statement corresponding 
    to the eight button will be shown along with a thank you statement. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    print('Thanks for playing!') : string
        A statement thanking the player.
    """  
    with out:
        print('\nHere is your task:\n' 
              '\nClean your desk\n')
        # Delays return statement to give player time to read task
        time.sleep(1.5)
        
    return print('Thanks for playing!')

# Allows this function to occur only when the eight button is clicked on
eight_button.on_click(eight_chosen)  