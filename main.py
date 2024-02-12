# Rock Paper Scisors

# Selection			Beats		Loses
#------------------------------------
# Rock				Scissors	Paper
#------------------------------------
# Paper				Rock		Scissors
#------------------------------------
# Scisors			Paper		Rock


# Rock Paper Scisors Lizard Spock

# Selection			Beats		Loses
#------------------------------------
# Rock				Scissors	Paper
#					Lizard		Spock
#------------------------------------
# Paper				Rock		Scissors
#					Spock		Lizard
#------------------------------------
# Scisors			Paper		Rock
#					Scissors	Spock
#------------------------------------
# Lizard			Spock		Rock
#					Paper		Scissors
#------------------------------------
# Spock				Scissors	Paper
#					Rock		Lizard

# imports
import numpy as np
import os
import time

# All available moves for the game.
move_Choices = ['Rock', 'Paper', 'Scissors',
                 'Lizard', 'Spock']
                 
# Pick a random number
def randomize(high_Num, low_Num=0):
    
    rng = np.random.Generator(np.random.PCG64())
    rng = np.random.default_rng()
    value = rng.random()
    value = rng.integers(low=low_Num, high=high_Num, size=1)
    value = int(value[0])
    
    return value
    
# Clear the screen
def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
        
# Make sure selection is an appropriate number
def selection_Validator(selection, nums_Allow):
    val_Selection = 0
    min_Range = nums_Allow - (nums_Allow - 1)
    max_Range = nums_Allow + 1
    
    def int_Check(num_to_Check, min_Range, max_Range):
        try:
            number = int(num_to_Check)                  # Make sure the number is an int
            return number, min_Range, max_Range
        except:                                         # If the choice is not an int, let the user pick again.
            valid_num = 0
            while valid_num == 0:                       # Let user continue to pick an input, until they choose an int.
                print(f'\nUser Entry, {num_to_Check}, is not a valid selection. Please choose a value between {min_Range} and {max_Range - 1}')
                number = input('?: ')
                try:
                    number = int(number)
                    return number, min_Range, max_Range
                except:
                    pass
    
    val_Selection = int_Check(selection, min_Range, max_Range)
    
    if val_Selection[0] not in range(min_Range, max_Range): # Make sure the int the user picked is in the correct range
        print(f'\nUser Entry, {val_Selection}, is not a valid selection. Please choose a value between {min_Range} and {nums_Allow}')
        selection = input('?: ')
        val_Selection = selection_Validator(selection, nums_Allow)
        return val_Selection[0], min_Range, max_Range
    else:
        return val_Selection[0], min_Range, max_Range

# Pick Game Version
def game_Version():
    clean()
    choice_Counter = 3                                                                              # For Rock Paper Scissors
    print('Choose the version to play')
    game_Type = input('1: Rock, Paper, Scissors\n2: Rock, Paper, Scissors, Lizard, Spock [1/2]?: ')
    game_Type = selection_Validator(game_Type, 2)
    if game_Type[0] == 2:
        choice_Counter = 5                                                                          # For Rock Paper Scissors Lizard Spock
    
    return choice_Counter
    
# Generate Computer Selection
def comp_Choose(counter):
  
    comp_Choice = randomize(counter, 0)
    
    return comp_Choice

# Player Selection Choice
def player_Choose(counter):

    print('Choose your option:')
    for i in range(counter):
        print(f'\n\t{i + 1}: {move_Choices[i]}')                                                    # Prints all choices from move_Choices, based on counter.
    
    player_Choice = input('Choice? :')
    player_Choice = selection_Validator(player_Choice, counter)
    player_Choice = player_Choice[0] - 1                                                            # Converts Valid choice to index position
    comp_Choice = comp_Choose(counter)                                                              # Computer gets randomly selected number based on counter
    
    return player_Choice, comp_Choice
    
# Display Selections

def draw_items(item_Choices):
    player = item_Choices[0]
    computer = item_Choices[1]
    rock = '''
                      ▓▓████████                  
                    ██    ░░░░▓▓██                
                  ██      ▒▒░░░░▓▓████            
                  ██      ▒▒▒▒▒▒    ▓▓██          
            ██████      ░░░░▒▒▒▒▒▒  ▓▓▓▓██        
        ▓▓▓▓          ▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓██        
      ▓▓▓▓    ▒▒▒▒    ░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓██      
      ▓▓    ░░▒▒      ▒▒  ░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓██      
    ▓▓    ░░▒▒▒▒  ░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓██      
    ▓▓    ░░▓▓    ▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓██      
    ▓▓    ▒▒▒▒▒▒  ░░░░▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▓▓▓▓██    
    ▓▓  ░░░░▒▒▒▒  ░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▓▓▓▓██    
  ▓▓░░▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒░░▓▓▓▓██    
  ▓▓▒▒  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓██    
▓▓▓▓░░▒▒▒▒▒▒▓▓▒▒░░░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓██  
▓▓░░  ▒▒▒▒▒▒▓▓░░░░░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██  
██░░▒▒▒▒▒▒▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓██  
██▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
██▓▓▒▒▒▒▓▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓██
██▒▒▓▓▒▒▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▓▓▒▒▓▓▓▓▓▓██
██▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓██  
  ██████████▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓██    
          ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░▓▓▓▓▓▓▓▓████      
            ████████████████████████████                                            
    '''
    
    paper = '''
                      ██████████                            
                  ████████████████                          
              ██████████▒▒▒▒▒▒▒▒████                        
            ████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                      
          ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                      
        ██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                      
      ██████▒▒░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                      
    ██████░░░░░░░░░░████▒▒▒▒▒▒▒▒▒▒████                      
    ████░░░░░░░░░░░░░░████▒▒▒▒▒▒████    ██████████          
    ████░░░░██████░░░░████▒▒▒▒████▒▒██████████████████      
    ████░░░░██▒▒██░░░░░░██▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████    
    ████░░░░██████░░░░░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████  
      ████░░░░░░░░░░░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
      ██████▒▒░░░░░░██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████
        ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████  
            ████████▒▒▒▒▒▒████████████████▒▒▒▒▒▒▒▒▒▒████    
                ████████████████████████████▒▒▒▒▒▒████      
                    ████████              ████▒▒████        
                                            ██████          
                                            ████     
    '''
    
    scissors = '''
      ████████▒▒                                                                          
    ▒▒██████████████▓▓                                                                      
  ░░██████▓▓▓▓▓▓████████                                                                    
  ████▓▓▒▒░░  ░░░░▒▒██████                                                                  
  ████░░            ░░██████                                                ▒▒████████▒▒    
  ████                  ████░░                                        ▒▒████████████████████
  ████                    ████                                ██████████████████████████▓▓▒▒
  ░░████                  ████░░                        ██████████████████████████▓▓▒▒░░    
    ████▒▒                ████░░                  ████████████████████████████▒▒░░          
      ██████              ████░░            ██████████████████████████████▓▓░░              
      ░░██████▓▓        ▓▓██████████  ░░████████████████████████████▓▓▒▒░░                  
        ░░████████████████████████████████████████████████████▓▓▒▒░░░░                      
            ▒▒██████████████████████████████████████████▓▓▒▒░░                              
                ░░▒▒▓▓▒▒▒▒  ░░▒▒████████████████████▒▒▒▒░░                                  
              ████████████████████████████████████████▒▒                                    
          ██████████████████████████████████████████████████                                
      ▒▒████████▒▒▒▒░░▒▒████████████▓▓████████████████████████████                          
      ████▓▓▒▒░░        ░░████░░░░░░░░  ░░▒▒██████████████████████████▒▒                    
    ████▒▒░░              ████░░            ░░▒▒▓▓██████████████████████████                
  ▓▓██▓▓░░                ████░░                  ░░▒▒████████████████████████▓▓            
  ████░░                ░░████░░                      ░░░░▓▓██████████████████████▓▓        
  ██▓▓                  ████▒▒                              ░░▒▒▓▓██████████████████████░░  
  ████                ▓▓████░░                                    ░░░░▓▓████████████████████
  ████              ██████▒▒                                            ░░▒▒▓▓██████████▓▓▒▒
  ░░██████▒▒  ▒▒▓▓██████▒▒░░                                                  ░░▒▒▒▒▒▒░░    
    ▒▒██████████████▓▓▒▒                                                                    
      ░░▒▒▓▓██▓▓▓▓▒▒░░                                                                      
     '''
     
    lizard = '''
            ████                                                    
      ████████████                                                  
      ██████  ██████                    ██                          
        ██████████████              ████                            
            ████████████            ██████                          
                ████████████████████████████                        
          ██████████████████████████████                            
            ██  ██████████████████████████                          
                  ██  ██████████████████████                        
            ██████      ████████████████████                        
          ██████              ██      ██████                        
            ██            ████      ████████                        
                        ████  ██    ██████                          
                                  ████████                          
                                ████████                            
                              ████████                              
                        ████████████                                
                  ████████████                                      
                                                        
    '''
    
    spock = '''
                 .......................... 
             ................................... 
          ......................................... 
        ............................................. 
       ................................................ 
      .................................................. 
     .................................................... 
     ......;%;%%%%%%%%%%%%%%%%%%%%%%%%%%%;%%.............. 
     .....;%%%;;;;%%%%%%%%%%%%%%%%%%;;;;%%%%..............% 
     .....%%%%%%%%;;;%%%%%%%%%%%%;;;%%%%%%%%%............%%% 
     /....%%%%%%%%%%%%;%%%%%%%%;%%%%%%%%%%%%%%..........;%%% 
     //...%%%a@@`  '@%%//%%%%%%%%@`  '@@a%%%%%%........;%/%% 
     //...%@@@@@aaa@@@%//%%%%%%@@@@aaa@@@@@%%%%%......%%/%% 
     //...%%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%....%%/%%% 
      //..%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%...%%/%%% 
       //.%%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%..%%/%%% 
        //%%%%%%%%%%%//%%%%%%%%%%%%%%%%%%%%%%%%%%..%/%%% 
         ;%%%%%%%%%%%//%%%%%%%%%;/%%%%%%%%%%%%%%%.%%% 
           %%%%%%%%%//%%%%%%%%%%%;/%%%%%%%%%%%%%%%% 
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/ 
             ;%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%// 
               %%%%%<<<<<<<<<<<<<<<<<%%%%%%%%%%;// 
                %%%%%<<<<<<<<<<<<<<<%%%%%%%%%%;/// 
                 %%%%%%%%%%%%%%%%%%%%%%%%%%%;///// 
                  %%%%%%%%%%%%%%%%%%%%%%%%;///////. 
                  /;%%%%%%%%%%%%%%%%%%%;////////.... 
                  ///;%%%%%%%%%%%%%%;////////......... 
    '''
    
    if player == 0:
        player = rock
    elif player == 1:
        player = paper
    elif player == 2:
        player = scissors
    elif player == 3:
        player = lizard
    else:
        player = spock
        
    if computer == 0:
        computer = rock
    elif computer == 1:
        computer = paper
    elif computer == 2:
        computer = scissors
    elif computer == 3:
        computer = lizard
    else:
        computer = spock
        
    
    print(f'PLAYER:{player}')
    print(f'\t\t\t\tCOMPUTER:{computer}')
    # if player_Win:
        # print(f'Player chose {move_Choices[player_C[0]]}, which {win_Verb} {move_Choices[comp_C[0]]}, Player Wins!')
    # elif comp_Win:
        # print(f'Computer chose {move_Choices[comp_C[0]]}, which {win_Verb} {move_Choices[player_C[0]]}, Computer Wins!')
    # else:
        # print(f'Player chose {move_Choices[player_C[0]]}, which does nothing to {move_Choices[comp_C[0]]}, it\'s a tie.')
# Calculate Winner

def find_Winner(item_Choices):
    # 0:Rock 1:Paper 2:Scissors 3:Lizard 4:Spock

    # Selection			Beats		Loses
    #------------------------------------
    # 0 				2,3     	1,4
    #------------------------------------
    # 1 				0,4 		2,3
    #------------------------------------
    # 2			        1,3 		0,4
    #------------------------------------
    # 3     			1,4		    0,2
    #------------------------------------
    # 4 				0,2     	1,3

    player_Win = 0
    comp_Win = 0
    users_Tie = 0
    win_Verb = ''
    
    outcome_Matrix = [
                    [0,2,3,'crushes', 'crushes'],   # Rock
                    [1,0,4,'covers', 'disproves'],   # Paper
                    [2,1,3,'cuts', 'decapitates'],   # Scissors
                    [3,1,4,'eats', 'poisons'],   # Lizard
                    [4,0,2,'vaporizes', 'smashes']    # Spock
                    ]
  
   
    player_C = outcome_Matrix[item_Choices[0]]
    comp_C = outcome_Matrix[item_Choices[1]]
   
    if comp_C[0] in player_C[1:3]:
        player_Win = 1
        if comp_C[0] == player_C[1]:
            win_Verb = player_C[3]
        else:
            win_Verb = player_C[4]
    elif player_C[0] in comp_C[1:3]:
        comp_Win = 1
        if player_C[0] == comp_C[1]:
            win_Verb = comp_C[3]
        else:
            win_Verb = comp_C[4]
    else:
        users_Tie = 1
        
    if player_Win:
        print(f'Player chose {move_Choices[player_C[0]]}, which {win_Verb} {move_Choices[comp_C[0]]}, Player Wins!')
    elif comp_Win:
        print(f'Computer chose {move_Choices[comp_C[0]]}, which {win_Verb} {move_Choices[player_C[0]]}, Computer Wins!')
    else:
        print(f'Player chose {move_Choices[player_C[0]]}, which does nothing to {move_Choices[comp_C[0]]}, it\'s a tie.')


# Game Loop

def main():
    done_play = 0
    play_Mode = game_Version()
    item_Choices = player_Choose(play_Mode)
    draw_items(item_Choices)
    find_Winner(item_Choices)
    print('\n\n\t\tPlay Again?')
    while done_play == 0:
        play_Again = input('\nY/N?')
        if play_Again.lower() == 'y':
            main()
        elif play_Again.lower() == 'n':
            print('GOODBYE!')
            done_play = 1
            break
        else:
            continue

main()
