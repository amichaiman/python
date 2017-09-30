#!/usr/bin/python3
import random

options = 'rock paper scissors'

game = 'y'
score = {'user' : 0, 
       'computer' : 0}
random.seed()


while game != 'n':
    rpc = input('%s? '%options)
    while rpc not in options.split():
        print ('invalid choice, try again: ')
        rpc = input('%s? '%options)
    computer = random.choice(options.split())
    if rpc == computer:
        winner = 'f'
    elif rpc == 'rock':
        if computer == 'paper':
            winner = 'computer'
        else:
            winner = 'user'
    elif rpc == 'paper':
        if computer == 'scissors':
            winner = 'computer'
        else:
            winner = 'user'
    else:
        if computer == 'rock':
            winner = 'computer'
        else:
            winner = 'user'
            
    if winner == 'computer':
        print ('\ncomputer chose %s, you lose\n'%computer)
        score['computer'] += 1
    elif winner == 'user':
        print('\ncomputer chose %s, you win\n'%computer)
        score['user'] += 1
    else:  
        print ('\nalse computer chose %s, it is a tie!\n'%computer)
    print (score)
    game = input('\nwanna play again? (y/n)')
    
    
    
print('\n\nfinal results:\n',score)

print ('and the winner is......')
if (score['user'] > score ['computer']):
    print ('YOU!')
elif (score['user'] < score ['computer']):
    print('COMPUTER')
else:
    print('NONE OF YOU!')