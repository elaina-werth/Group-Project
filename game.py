#create the game

def game(random_number, MIN, MAX, player1, player2):
    #accepts an integer for number to be guessed, two inteers for min and max to validate range
    #players take turns guessing the number and receive feedback
    #tracks number of turns and validates out-of-range guesses
    print ("Welcome to the game!")
    
    keepgoing = 1
    
    while keepgoing == 1:
        #player 1 turn
        print(player1, ": Guess a number between", MIN, "and", MAX, end = '')
        player_1_choice = int(input(": "))
        
        #validate
        if player_1_choice < MIN or player_1_choice > MAX:
            print ("Oops! Please enter a valid number." player1, "Guess a number between", MIN, "and", MAX, end = '')
        player_1_choice = int(input(": "))
        
        if player_1_choice < random_number:
            print("A little higher!")
        elif player_1_choice > random_number:
            print("A little lower!")
        else:
            print ("Congratulations, you have guessed the number!")
            keepgoing = 0
            break
            
        #player 2 turn
        print (player2, ": Guess a number between", MIN, "and", MAX, end = '')
        player_2_choice = int(input(": "))
        
        if player_2_choice < random_number:
            print("A little higher!")
        elif player_2_choice > random_number:
            print("A little lower!")
        else:
            print ("Congratulations, you have guessed the number!")
            keepgoing = 0
        