def menu():
    #menu accepts no arguments
    #it displays a menu to the user, prompts for a selection
    #menu returns a value for choice
    
    #display menu
    print('You can:')
    print('Create a new game,(1)')
    print('Choose a new range,(2)')
    print('Or Exit(3)\n')
    
    #collect input from user
    #life sucks
    choice = int(input('What would you like to do? '))
    while choice > 3 or choice < 1:
        choice = int(input('What would you like to do? (pick 1,2, or 3) '))
    return choice