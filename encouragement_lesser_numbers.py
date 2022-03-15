"""Set of numbers displayed after selecting red or green after encouragement."""

import ipywidgets as widgets
from ipywidgets import VBox, HBox
from IPython.display import display
import time

# Set of buttons shown after player selects red or green
one_button = widgets.Button(description='1')
two_button = widgets.Button(description='2')
five_button = widgets.Button(description='5')
six_button = widgets.Button(description='6')
out = widgets.Output()

# Arranges the buttons into a 2x2 table
left_box = VBox([one_button, five_button])
right_box = VBox([two_button, six_button])
out_lesser = HBox([left_box, right_box])
        
display(out_lesser, out)

def one_chosen(clicked):
    """After the one button is chosen, a statement corresponding 
    to the one button will be shown along with a thank you statement. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    print('Thanks for playing :)') : string
        A statement thanking the player.
    """    
    with out: 
        print('\nHere are your words of encouragement:\n' 
              '\nYou can do it!\n')
        # Delays return statement to give player time to read 
        # words of encouragement
        time.sleep(1.5)
        
    return print('Thanks for playing :)')

# Allows this function to occur only when the one button is clicked on 
one_button.on_click(one_chosen)

def two_chosen(clicked):
    """After the two button is chosen, a statement corresponding 
    to the two button will be shown along with a thank you statement. 
    
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
        print('\nHere are your words of encouragement:\n' 
              '\nSending good vibes your way~~\n')
        # Delays return statement to give player time to read 
        # words of encouragement        
        time.sleep(1.5)
        
    return print('Thanks for playing!')

# Allows this function to occur only when the two button is clicked on 
two_button.on_click(two_chosen)

def five_chosen(clicked):
    """After the five button is chosen, a statement corresponding 
    to the five button will be shown along with a thank you statement. 
    
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
        print('\nHere are your words of encouragement:\n' 
              '\nYou’re beautiful just the way you are :)\n')
        # Delays return statement to give player time to read 
        # words of encouragement 
        time.sleep(1.5)
        
    return print('Thanks for playing!')

# Allows this function to occur only when the five button is clicked on 
five_button.on_click(five_chosen)   

def six_chosen(clicked):
    """After the six button is chosen, a statement corresponding 
    to the six button will be shown along with a thank you statement. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    print('Thanks for playing :)') : string
        A statement thanking the player.
    """  
    with out:
        print('\nHere are your words of encouragement:\n' 
              '\nI have faith in you!\n')
        # Delays return statement to give player time to read 
        # words of encouragement
        time.sleep(1.5)
        
    return print('Thanks for playing :)')

# Allows this function to occur only when the six button is clicked on         
six_button.on_click(six_chosen)