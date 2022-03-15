"""Set of colors displayed after selecting fortune."""

import ipywidgets as widgets
from ipywidgets import VBox, HBox
from IPython.display import display

# Set of buttons shown after player selects a category
red_button = widgets.Button(description='red \U0001F534')
green_button = widgets.Button(description='green \U0001F7E2')
blue_button = widgets.Button(description='blue \U0001F535')
purple_button = widgets.Button(description='purple \U0001F7E3')
out = widgets.Output()

# Arranges the buttons into a 2x2 table
left_box = VBox([red_button, green_button])
right_box = VBox([blue_button, purple_button])
out_colors = HBox([left_box, right_box])

display(out_colors, out)

def red_button_chosen(clicked):
    """After the red button is chosen, player will be asked to select 
    a number. A set of numbers corresponding to the red button will
    be shown. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    none
    """    
    with out:
        print('Select a number')
        # A module leading to the set of numbers corresponding
        # to the red button.
        import my_module.fortune_lesser_numbers

# Allows this function to occur only when the red button is clicked on     
red_button.on_click(red_button_chosen)

def green_button_chosen(clicked):
    """After the green button is chosen, player will be asked to select 
    a number. A set of numbers corresponding to the green button will
    be shown. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    none
    """    
    with out:
        print('Select a number')
        # A module leading to the set of numbers corresponding
        # to the green button. 
        import my_module.fortune_lesser_numbers

# Allows this function to occur only when the green button is clicked on 
green_button.on_click(green_button_chosen)

def blue_button_chosen(clicked):
    """After the blue button is chosen, player will be asked to select 
    a number. A set of numbers corresponding to the blue button will
    be shown. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    none
    """   
    with out:
        print('Select a number')
        # A module leading to the set of numbers corresponding
        # to the blue button. 
        import my_module.fortune_greater_numbers

# Allows this function to occur only when the blue button is clicked on 
blue_button.on_click(blue_button_chosen)

def purple_button_chosen(clicked):
    """After the purple button is chosen, player will be asked to select 
    a number. A set of numbers corresponding to the purple button will
    be shown. 
    
    Parameters
    ----------
    clicked : Button (ipywidgets.widgets.widget_button.Button)
        Allows function to run if button is clicked.
    
    Returns
    -------
    none
    """
    with out:
        print('Select a number')
        # A module leading to the set of numbers corresponding
        # to the purple button. 
        import my_module.fortune_greater_numbers

# Allows this function to occur only when the purple button is clicked on
purple_button.on_click(purple_button_chosen)