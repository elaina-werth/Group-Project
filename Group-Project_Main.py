#Group-Project_Main
from menufunct import *
from getnum import *
from limit import *
import random
from get_name2 import *
from game import *

def main():
    #main accepts no arguments
    #it calls all functions necessary to create a number-guessing game
    
    #define constants for menu options and default range
    MIN = 1
    MAX = 1000
    
    #create a variable to start or stop the loop
    keep_going = 1
    
    #call menu
    menu_choice = menu()
    
    #loop menu
    while keep_going == 1:
        if menu_choice == 1:
            #collect names, the number to be guessed, and begin game
            player1, player2 = get_name2()
            random_number = get_number(MIN, MAX)
            game (random_number,MIN, MAX, player1, player2)
            menu_choice = menu()
        elif menu_choice == 2:
            MIN, MAX = limit()
            print()
            menu_choice = menu() #pull up menu again after changing limit
            print()
        elif menu_choice == 3:
            print("Exiting...\nThank you for playing the number game!")
            keep_going = 0 #leave loop
        else: #validate
            print("Oops! It looks like your choice wasn't a valid option.\n")
            menu_choice = menu()
