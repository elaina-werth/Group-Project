#Group-Project_Main
from menufunct import *


def main():
    #main accepts no arguments
    #it calls all functions necessary to create a number-guessing game
    
    #define constants for menu options and default range
    MIN = 1
    MAX = 1000
    
    #call menu
    menu_choice = menu()
    
    if menu_choice == 1:

        game (MIN, MAX)
    elif menu_choice == 2:
        MIN, MAX = limit()
    elif menu_choice == 3:
        print("Exiting...\nThank you for playing the number game!")
    else: #validate
        print("Oops! It looks like your choice wasn't a valid option.")
        menu_choice = menu()
