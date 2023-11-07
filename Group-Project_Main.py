#Group-Project_Main
from menufunct import *
from getnum import *
from limit import *
import random
from get_name2 import *

def main():
    #main accepts no arguments
    #it calls all functions necessary to create a number-guessing game
    
    #define constants for menu options and default range
    MIN = 1
    MAX = 1000
    
    keep_going = 1
    
    #call menu
    menu_choice = menu()
    
    while keep_going == 1:
        if menu_choice == 1:
            random_number = getnumber(MIN, MAX)
            game (MIN, MAX)
        elif menu_choice == 2:
            MIN, MAX = limit()
            menu_choice = menu() #pull up menu again after changing limit
            print()
        elif menu_choice == 3:
            print("Exiting...\nThank you for playing the number game!")
            keep_going = 0
        else: #validate
            print("Oops! It looks like your choice wasn't a valid option.\n")
            menu_choice = menu()
