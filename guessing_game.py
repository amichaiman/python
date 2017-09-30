#!/usr/bin/python3

import random

continue_game = 'y'

rand_num = random.randint(1,11)

while continue_game != 'n':
    users_num = int(input('\nEnter number between 1 and 10: '))
    while users_num > 10 or users_num < 1:
        users_num = int(input('\nInvalid choice, try again: '))
    
    if users_num > rand_num:
        continue_game = input('\nyou guessed too high, wanna try again? (y/n)')
    elif users_num < rand_num:
        continue_game = input('\nyou guessed too low,wanna try again? (y/n) ')
    else:
        print('\n\nnice! that was the right number! \n\n')
        continue_game = 'n'
    
        
        
        
