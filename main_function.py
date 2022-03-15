"""The main function for doing my project."""

import time

def start():
    """Starts the cootie catcher game by asking for player's name
    and having them choose a category. After a category is chosen, 
    the player is also asked to choose a color"
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
    """
    
    # Asks for name and provides introduction message with information about the game
    name = input("Welcome! What's your name? ")
    print("\nHello {}! Excited to have you here to play cootie catcher.\n"
          "There are three categories to choose from:\n"
          "fortune (1), words of encouragement (2), fun task (3).\n".format(name))
    
    # Delays the next statement to give the player time to read previous statement 
    time.sleep(2.1)
    category = int(input("Please choose a category according to its corresponding number: "))
    
    # Different categories lead to different modules that display the colors
    if category == 1:
        print('\nSelect a color\n')
        import my_module.fortune_color

    elif category == 2:
        print('\nSelect a color\n')
        import my_module.encouragement_color
        
    elif category== 3:
        print('\nSelect a color\n')
        import my_module.task_color
        
    else:
        print("\nPlease enter a number from 1-3. Try again.\n")
    