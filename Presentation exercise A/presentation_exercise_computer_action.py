

NUM_PLAYER_BALLS = 0
NUM_OPPONENT_BALLS = 0
COMPUTER_POINTS = 0
HUMAN_POINT = 0 

def points_gained(human_action, computer_action):
    if(human_action == "throw"  and computer_action == "throw"):
        COMPUTER_POINTS += 1
        HUMAN_POINT = +1   
        print("1 point for each side!")
    elif (human_action == "pickup" and computer_action == "throw"):
        print("computer gets 1 point!")
        COMPUTER_POINTS += 1
    elif (computer_action == "pickup" and human_action == "throw"):
        HUMAN_POINT +=1
        print("human gets 1 point!") 
    if not (human_action == "throw" and computer_action == "throw"): 
        print()
    elif not(human_action == "pickup" and computer_action == "throw") or (computer_action == "pickup" and human_action == "throw"):
        print()

def get_human_action(NUM_PLAYER_BALLS, NUM_OPPONENT_BALLS):
  
    human_action = input("Which action will you take? (throw, dodge, or pickup) ")
    
    valid_action = True
    
    #This set of code makes sure user enters a valid action given the constraints
    #and asks them to reenter until they give a valid action
    if (human_action == "pickup" and NUM_PLAYER_BALLS == 3):
        valid_action = False
        
    elif (human_action == "throw" and NUM_PLAYER_BALLS == 0):
        valid_action = False
        
    elif (human_action == "throw" or human_action == "dodge" or human_action == "pickup"):
        valid_action = True
        
    else:
        valid_action = False
    
    while not valid_action == True:
        print("Invalid input!")
        human_action = input("Please re-enter action: ")
        
        if (human_action == "pickup" and NUM_PLAYER_BALLS == 3):
            valid_action = False
            
        elif (human_action == "throw" and NUM_PLAYER_BALLS == 0):
            valid_action = False
            
        elif (human_action == "throw" or human_action == "dodge" or human_action == "pickup"):
            valid_action = True
            
        else:
            valid_action = False
            
    if human_action == "throw":
        NUM_PLAYER_BALLS -= 1
        
    if human_action == "pickup":
        NUM_PLAYER_BALLS += 1
            
    return (human_action)

import random

def get_computer_action(NUM_PLAYER_BALLS, NUM_OPPONENT_BALLS):
    pickup = "pickup"
    dodge = "dodge"
    throw = "throw"
    
    computer_action = pickup or dodge or throw
    
    valid_action = True
 
    if (NUM_PLAYER_BALLS <= 2):
        computer_action = (dodge)
        print("the computer chose:", computer_action)
        valid_action = True
    
    elif (NUM_OPPONENT_BALLS == 0):
        computer_action = random.choice( pickup or dodge)
        print("the computer chose:", computer_action)
        valid_action = True

    else:
        valid_action = False
        
    if computer_action == "throw":
        NUM_OPPONENT_BALLS -= 1
    if computer_action == "pickup":
        NUM_OPPONENT_BALLS  += 1

    return (computer_action)